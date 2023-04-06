import tkinter as tk
import cryptography.fernet as fernet
from datetime import datetime
import time
from pyinjector import inject
import psutil
import os
import urllib.request
from PIL import ImageTk, Image
import os
import webbrowser
from os.path import exists
kutyagecinemmegy = "<!DOCTYPE HTML>"
#time, for logging events! (Variable name : "now")
now = datetime.now()
def injeect():
        global errmsg
        try:file_exists = exists('cheeto.dll')
        except FileNotFoundError:
            print("FILENOTFOUND PASSED")
            pass
        if file_exists == False:
            print(f"{now} Cheat not found!(cheeto.dll) Downloading!")
            urllib.request.urlretrieve('https://cdn-153.anonfiles.com/x4BbVehcza/36f94fbd-1680277564/RyzeXTR%286%29.dll', 'cheeto.dll')

            with open('cheeto.dll', encoding="utf-8") as myfile:
                print("OPENING DLL")
                if '<!DOCTYPE HTML>' in myfile.read():
                    e.destroy()
                    print("Download the cheat (the site you just got directed to is a good place to download it from :)\nPut the dll in the same folder as this injector, and rename it to 'cheeto'!\n Press ENTER to exit the code.")
                    webbrowser.open('https://anonfiles.com/x4BbVehcza')
                    input("Press ENTER to exit!")
                    quit()
        else:
            print(f"{now} Cheat found, proceeding!")
        print(f"{now} Game starting!")
        webbrowser.open('steam://rungameid/730')
        #discord cdn
        #webbrowser.open('https://cdn-151.anonfiles.com/15z8J9h0za/c14bdbe2-1680197723/RyzeXTR%281%29.dll')  # Go to example.com
        try:
            print(f"{now} 20s till inject")
            time.sleep(20)
            pathl = os.getcwd()
            process_name = "csgo"
            pid = None

            for proc in psutil.process_iter():
                if process_name in proc.name():
                    pid = proc.pid
                    break

            inject(pid,"cheeto.dll")
        except AssertionError:
            #should be returning error msg to output in tkinter IDK whats wrong here :()
            print(f"{now} ___C.ERR. CS:GO didnt launch! wtf? Is it downloaded?")
            errmsg = "Err:1 process not found!"

#pid = csgo pid
#usrname check, exit if name exists, checked by pass
login = ['123']
access = False
def check():
    global usrn
    global access
    usrn = e1.get()
    if usrn in login:
        print(f"{now} Logged in as : {usrn}")
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
    errmsg = tk.StringVar()
    q2 = tk.Label(e, text="For logs, check terminal/cmd opened with this injector!" ,fg="red",bg="black")
    q2.pack(side="left")

    
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
        print(f"{now} ____R.ERR. You dumbass didnt i just tell you to put the image into the same folder as the script?!\nIf you didnt know the R before the 'err' means retard")
        pass

    #pid for csgo pid
 
    tk.mainloop()
