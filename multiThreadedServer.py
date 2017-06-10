from socket import *
from thread import *
 
host = 'localhost'  
port = 52000      #Use port > 1024, below it all are reserved

sock = socket()
sock.bind((host, port)) 
sock.listen(2)  #2 denotes the number of clients can queue

print("Server listening")

while True:
    conn, addr = sock.accept()     # Establish connection with client.
    print 'Got connection from', addr
	
    data = conn.recv(1024) #1024 stands for bytes of data to be received
    print data

conn.close()
sock.close()
