from zope.interface import Interface
from five import grok

grok.templatedir('templates')

class edxView(grok.View):
    grok.context(Interface)

