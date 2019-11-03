#! /usr/bin/python3
import socket
import threading
class create_server(threading.Thread):
    def __init__(self, filenames):
        threading.Thread.__init__(self)
        self.filename = filenames
    def run(self):
        port = 12345                                                      
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = socket.gethostname()                                                                                        
        IP = socket.gethostbyname(host)                                        
        serversocket.bind((host, port))            
        serversocket.listen(1)                     
        print('Server listening....')
        print('MY IP is :',IP,'and my PORT is:',port)
        while True:
            # filename=['first file','second file','third file']
            filename_string = ",".join(self.filename)
            clientsocket, addr = serversocket.accept()     
            print('Got connection from', addr)
            clientsocket.send(filename_string.encode())
            data = clientsocket.recv(1024)
            data = data.decode()
            print("Client requested : ", data)
            filetomanage = 'send.txt' #file to be sent
            with open(filetomanage, 'rb') as f:
                packet = f.read(4096)
                while packet:
                    clientsocket.send(packet)
                    packet = f.read(4096)
            f.close()
            clientsocket.close()