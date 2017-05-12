from xml.sax.handler import ContentHandler
from xml.sax import parse


class HeadlineHandler(ContentHandler):
    # 放注释的地方
    in_headline = False

    def __init__(self, headlines):
        ContentHandler.__init__(self)
        self.headlines = headlines
        self.data = []

    def startElement(self, name, attrs):
        if name == 'h1':
            self.in_headline = True

    def endElement(self, name):
        if name == 'h1':
            text = ''.join(self.data)


parse('website.xml', TestHandler())
