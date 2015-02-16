from socket import *
serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(True)
print ('Ready to serve...')
while True:
	print ('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024)#Fill in start #Fill in end
		
		print(message)
		filename = message.split()[1]
		print(filename)
	except IOError:
		pass

serverSocket.close()
