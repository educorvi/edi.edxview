# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from edi.edxview.testing import EDI_EDXVIEW_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that edi.edxview is properly installed."""

    layer = EDI_EDXVIEW_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if edi.edxview is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'edi.edxview'))

    def test_browserlayer(self):
        """Test that IEdiEdxviewLayer is registered."""
        from edi.edxview.interfaces import (
            IEdiEdxviewLayer)
        from plone.browserlayer import utils
        self.assertIn(IEdiEdxviewLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EDI_EDXVIEW_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['edi.edxview'])

    def test_product_uninstalled(self):
        """Test if edi.edxview is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'edi.edxview'))

    def test_browserlayer_removed(self):
        """Test that IEdiEdxviewLayer is removed."""
        from edi.edxview.interfaces import \
            IEdiEdxviewLayer
        from plone.browserlayer import utils
        self.assertNotIn(IEdiEdxviewLayer, utils.registered_layers())
