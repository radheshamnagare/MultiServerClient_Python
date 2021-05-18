import socket
import signal
import sys
import errno
import os.path
from os import path
import threading 


#constant byte size
SIZE = 1024
#we shall get port no from command line
if(len(sys.argv) != 2):
    print(f"python3 {sys.argv[0]} <PORT>")
    exit(0)
#signal handler
def signal_handler(sing,frame):
    print("exit")
    exit(0)

#if signal ctr+c happen
signal.signal(signal.SIGINT,signal_handler)    
#handle each new client
def newClientSocketHandler(clientSocket,ip,dir_path,file_path):
    fd = -1
    try:
        if(path.exists(file_path)):
            msg = b'ok'
            clientSocket.send(bytearray(msg));
            fd = open(file_path,'rb')
        #send bytes to the client
            while True:
                byte = fd.read(SIZE)
                if(byte.__len__() ==0):
                    break
                #sending bytes    
                no_of_byte=clientSocket.send(bytearray(byte))
                #i shall back for inproper packate send

        else:
            msg = (b'-1e')
            clientSocket.send(bytearray(msg))    
                          
    except Exception as error: 
       #if any others error occer then send acknowlegment to client    
        msg = (b'-2e')
        if clientSocket!=-1:
            clientSocket.send(bytearray(msg))    
        print(error.__str__())
    finally:
        if(fd != -1):
            fd.close()
        if(clientSocket!=-1):    
            clientSocket.close()
        

try:
    #to hold ip address
    ip =None
    #represent the host
    Host = str(socket.INADDR_ANY)
    #represent port
    Port = sys.argv[1]
    #server socker discripter initilize -1
    serverSocket = -1    
    #creating socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print(serverSocket)
    print("[+]SOCKET CREATED")
    #create datasourse directory of server using port no 
    dir = "d"+str(Port)
    #if directory not exist then creating server directory
    if path.exists(dir) == False:
        os.makedirs(dir)
    #represent directory    
    dir_path = dir+"/"
    #bind host & port pair to socket
    serverSocket.bind((Host,int(Port)))
    print("[+]SOCKET BIND")
    #listening at least 10 client
    serverSocket.listen(10)
    print("[+]LISTENIG 10 CLIENT")
    #Accept client connections  

    while True :
        #accepting the client connections    
        clientSocket ,ip = serverSocket.accept()
        print(f"\nNEW CLIENT CONNECTION :{ip}")
        #get file requirement from client
        file_name = clientSocket.recv(SIZE)
        file_name = file_name.decode('ascii')
        #handle each new client using thread
        threading._start_new_thread(newClientSocketHandler,(clientSocket,ip,dir_path,dir_path+file_name))
except Exception as error:
    print("[-]",error.__str__())    
finally:
    if(serverSocket != -1):
        serverSocket.close()    
   






