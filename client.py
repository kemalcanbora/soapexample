from zeep import Client
client = Client('http://localhost:7789?wsdl')
result = client.service.say_top(100, 34321)
print result