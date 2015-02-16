#import socket module
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(True)
#Prepare a sever socket
#Fill in start
#Fill in end
print ('Ready to serve...')
while True:
	#Establish the connection
	print ('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	try:
                message = connectionSocket.recv(1024)#Fill in start #Fill in end
		print(message)
		##filename = message.split()[1]
		##f = open(filename[1:])
		##outputdata = #Fill in start #Fill in end
		#Send one HTTP header line into socket
		#Fill in start
		#Fill in end
		#Send the content of the requested file to the client
		#for i in range(0, len(outputdata)):
		#connectionSocket.send(outputdata[i])
		#connectionSocket.close()
	except IOError:
                pass
		#Send response message for file not found
		#Fill in start
		#Fill in end
		#Close client socket
		#Fill in start
		#Fill in end

serverSocket.close()
