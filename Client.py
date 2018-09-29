import socket
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

Host = '127.0.0.1'
Port = 8080

Sock.connect((Host,Port))
print("Cautari posibile: telefoane mobile, tablete, telefoane mobile, Samsung")
while 1:
	msg = input('>> ')
	Sock.send(msg.encode())