import socket                   # Import socket module
while True:
    s = socket.socket()             # Create a socket object
    host = socket.gethostname()     # Get local machine name
    # host = '172.16.45.164'
    port = 12345                    # Reserve a port for your service.
    s.connect((host, port))			#client is connected with server
    print("Press e to exit the program")
    file_string = s.recv(1024)		#receiving the filelist from server
    file_string = file_string.decode()
    file_list = file_string.split(',')
    i=1
    for files in file_list:
        print(i,'. ',files, end="\n")
        i+=1
    print("Enter your choice : ")
    inputdata = input()
    s.send(inputdata.encode())
    filetomanage = 'receive.txt'
    with open(filetomanage,'wb+') as f:
        packet = s.recv(4096)
        while packet:
            f.write(packet)
            packet = s.recv(4096)
    f.close()
    print("File received!")
    print("File has been received. You want more files ? Y/N")
    ch=input()
    s.close()
    if(ch =='N' or ch=='n'):
        break