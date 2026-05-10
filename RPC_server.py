import xmlrpc.server
import math

def factorial(n):
    if n<0:
        return "negative no. factorial not possible"
    return math.factorial(n)

server=xmlrpc.server.SimpleXMLRPCServer(("localhost",8000))

print("listening on port 8000")

server.register_function(factorial,"factorial")

server.serve_forever()