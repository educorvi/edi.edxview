.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
edi.edxview
==============================================================================

These product provides a browser view for rendering Plone pages in a pure getbootstrap layout. This is useful if you want to embed pages in a foreign system via iFrame.

Usage
-----

You can append "@@edxview" to your URL and embed your pages with the following code:

<iframe src="http://my.plone.site/page/@@edxview" ..></iframe>


Examples
--------

An example usecase is to embed Plone pages with content you need in more then one mooc.


Installation
------------

Install edi.edxview by adding it to your buildout::

    [buildout]

    ...

    eggs =
        edi.edxview


and then running ``bin/buildout``


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: walther.educorvi@gmail.com


License
-------

The project is licensed under the GPLv2.
