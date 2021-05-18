import socket
import sys
import signal
import os.path
from os import path

#constant size
SIZE = 1024
#accepting ip and host from cmd
if(len(sys.argv) !=3):
	print(f"python3 {sys.argv[0]} <IP> <PORT>")
	exit(0)
def signal_handler(sing,frame):
    print("exit")
    exit(0)

#handling ctr+c signal
signal.signal(signal.SIGINT,signal_handler)



try:

	flag = 0
	#representing to file descripter and initilize to -1
	fd = (-1)
	#representing to client socket and initilize to -1
	clientSocket = (-1)
	#representing to host/ip
	Host = sys.argv[1]
	#port number
	Port = int(sys.argv[2])
	#creating client socket
	clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#client local storage directory
	dir = "localStorage"
	#if directory not exist
	if(path.exists(dir) == False):
		os.makedirs(dir)	
	#connect to the server/machine socket	
	clientSocket.connect((Host,Port))
	#getting input required file
	file = input("Requested File :")
	dir_path = dir+"/"+file
	
	#send file request to machine/server
	no_of_byte = clientSocket.send(file.encode('ascii'))
	file_exist = clientSocket.recv(SIZE);
	if file_exist == b'ok':
		#open file in append binary mode
		fd = open(dir_path,mode="ab")
		while True:
			#receving byte from server	
			byte = clientSocket.recv(SIZE)
			to_data = byte
			#check receving byte zero
			if to_data.__len__() ==0:
				break
				#check error code in byte format	
			elif to_data == b'-2e':
				flag = -1
				print('[-]SERVER ERROR')
				break
			#write data in file	
			else:
				fd.write(byte)
	else:
		if file_exist == b'-1e':
			flag = -1
			print(f'[-]FILE NOT FOUND ON SERVER :{file}')
			#check error code in byte format	
		elif file_exist == b'-2e':
			flag = -1
			print('[-]SERVER ERROR')	

	if(flag == 0):
		print("[+] FILE SUCCESFULY DOWNLOAD")
	
	print("EXIT Y|N :")
	while True:
		answer = input("-->")
		if(answer == 'Y' or answer == 'y'):
			break

					
except Exception as error:
	print(error.__str__())
finally:
	if(clientSocket !=-1):
		clientSocket.close()
	clientSocket.close()
	if(fd != -1):	
		fd.close()