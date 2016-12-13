from soaplib.service import rpc
from soaplib.service import DefinitionBase
from soaplib.serializers.primitive import String, Integer ,Float
from soaplib.wsgi import Application
from soaplib.serializers.clazz import Array
import soaplib
from flask import Flask
app = Flask(__name__)

class Toplama(DefinitionBase):
    @rpc(Integer, Integer, _returns=Integer)
    def say_top(self, a, b):
        sonuc=a+b
        return str(sonuc)




if __name__=='__main__':
    try:
        from wsgiref.simple_server import make_server
        server = make_server('localhost', 7789, Application([Toplama], 'tns'))
        print server
        server.serve_forever()
        app.run(host='localhost')
    except ImportError:
        print "Error: example server code requires Python >= 2.5"

