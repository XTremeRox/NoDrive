#! /usr/bin/python3
import socket
import threading
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from server import *
import netifaces

def browsefunc():
    filenames = filedialog.askopenfilenames()
    print(filenames)
    if filenames:
        print("File names received")
        choosebutton.config(state="disabled", text="CHOOSED")
        serverbutton.config(state="enabled")
        global t1
        s = create_server(filenames)
        t1 = threading.Thread(target=s.run)
        t1.daemon = True
    # pathlabel.config(text=filename)
def start_and_disable():
    serverbutton.config(state="disabled")
    t1.start()

def start_server_thread():
    serverwindow = Toplevel(root)
    serverwindow.geometry("300x200+500+150")
    root.withdraw()
    serverwindow.title('Server Window')
    serverwindow.iconbitmap("no_drive_icon.ico")
    frame = Frame(serverwindow)
    frame.pack()
    label3 = Label(frame, text = "IP : "+myip)
    label3.config(foreground = "blue", font = "Verdana 15 bold", justify=CENTER)
    label3.place(relx=0.5, rely=0.1, anchor=CENTER)
    global serverbutton, choosebutton
    serverbutton = Button(frame, text = 'START SERVER', command = lambda : start_and_disable(), state="disabled")
    serverbutton.place(relx=0.5, rely=0.5, anchor=CENTER)
    choosebutton = Button(frame, text = 'CHOOSE', command = lambda : browsefunc())
    choosebutton.place(relx=0.5, rely=0.8, anchor=CENTER)
    frame.config(height = 200, width = 300)
    frame.config(relief = RIDGE)
    serverwindow.protocol("WM_DELETE_WINDOW", lambda: root.destroy())
    serverwindow.resizable(False, False)

myip = socket.gethostbyname(socket.gethostname())  
root = Tk()
root.geometry("500x400+500+150")
root.iconbitmap("no_drive_icon.ico")
root.resizable(False, False)
root.title("NoDrive")
style = Style() 
style.configure('TButton', font = ('calibri', 24, 'bold'), borderwidth = '4') 
style.map('TButton', foreground = [('active', 'blue')], background = [('active', 'red')]) 
root.grid_columnconfigure(1, weight = 1)
label = Label(root, text = "Send or Recive Files using NoDrive")
label.config(foreground = "red", font = "Verdana 15 bold", justify=CENTER)
label2 = Label(root, text = "Your IP : "+myip)
label2.config(foreground = "green", font = "Verdana 15 bold", justify=CENTER)
label.grid(row = 0, column = 1)
label2.grid(row = 1, column = 1)
button1 = Button(root, text = 'SEND*', command = start_server_thread) 
button1.grid(row = 2, column = 1, pady = 50) 
button2 = Button(root, text = 'RECEIVE', command = None) 
button2.grid(row = 3, column = 1) 
label3 = Label(root, text = "*Your IP needs to be reachable by the client")
label3.config(foreground = "red", font = "Verdana 9 bold", justify=LEFT)
label3.grid(row = 4, column = 1, pady = "50")

root.mainloop()