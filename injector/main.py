#imports
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
import playsound as ps
access = 0
def main():
    #creates m win.
    m = tk.Tk()
    m.resizable(False,False)
    inj = tk.StringVar()
    #m.geometry , settings
    m.title("Injector")
    m.geometry('500x400')
    m.config(bg="Black")
    #actual code
    #injection process
    def injection():
        try:
            file_exists = exists('cheeto.dll')
        except FileNotFoundError:
            print("FILENOTFOUND PASSED")
            pass
        if file_exists == False:
            now = datetime.now()
            print(f"{now} Cheat not found!(cheeto.dll) Downloading!")
            #main cheat downloader ---- must be a cdn, it wont work unless its a static cdn
            urllib.request.urlretrieve('https://cdn-153.anonfiles.com/t45302idz2/ff7d1e86-1681026007/RyzeXTR%282%29.dll', 'cheeto.dll')
            try:
                with open('cheeto.dll', encoding="utf-8") as myfile:
                    print("OPENING DLL")
                    if '<!DOCTYPE HTML>' in myfile.read():
                        m.destroy()
                        print("Download the cheat (the site you just got directed to is a good place to download it from :)\nPut the dll in the same folder as this injector, and rename it to 'cheeto'!\nPress ENTER to exit the code.")
                        webbrowser.open('https://anonfiles.com/t45302idz2/RyzeXTR_2_dll')
                        input("Press ENTER to exit!")
                        quit()
            except UnicodeDecodeError:
                now = datetime.now()
                print(f"{now} UNICODEDECODEERR")
                global access
                access = access + 1
                pass

        else:
            if access == 1:
                now = datetime.now()
                print(f"{now} The right file was downloaded")
                pass
            else:
                now = datetime.now()
                print(f"{now} Cheat found, scanning then proceeding!")
            try:
                with open('cheeto.dll', encoding="utf-8") as myfile:
                    now = datetime.now()
                    print(f"{now} OPENING DLL")
                    if '<!DOCTYPE HTML>' in myfile.read():
                        m.destroy()
                        print(f"{now} File corrupted")
                        print("Download the cheat (the site you just got directed to is a good place to download it from :)\nPut the dll in the same folder as this injector, and rename it to 'cheeto'!\nPress ENTER to exit the code.")
                        webbrowser.open('https://anonfiles.com/t45302idz2/RyzeXTR_2_dll')
                        input("Press ENTER to exit!")
                        quit()
            except UnicodeDecodeError:
                now = datetime.now()
                print(f"{now} File scanned: the file is uncorrupted, proceeding!")
                pass
        now = datetime.now()
        print(f"{now} Game starting!")
        webbrowser.open('steam://rungameid/730')
        try:
            now = datetime.now()
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
            ps.playsound('bounceera.wav')
            inj.set("Injected, have fun!")
        except AssertionError:
            now = datetime.now()
            print(f"{now} ___C.ERR. CS:GO didnt launch! wtf? Is it downloaded?")
            errmsg = "Err:1 process not found!"
    tk.Label(m, text="Injector",bg="Black",fg="White").pack()
    tk.Label(m, textvariable=inj,bg="Black",fg="Red").pack()
    tk.Label(m, text="Owner/Developer:",bg="Black",fg="White").pack()
    try:
        img = ImageTk.PhotoImage(Image.open("assets/CRDEPNG.png"))
        panel = tk.Label(m, image = img)
        panel.pack()
    except FileNotFoundError:
        now = datetime.now()
        print(f"{now} ____R.ERR. You dumbass didnt i just tell you to put the image into the same folder as the script?!\nIf you didnt know the R before the 'err' means retard")
        pass
    b = tk.Button(m, text="Inject",command=injection,width=45,pady=10)
    b.pack(side = tk.BOTTOM)
    m.mainloop()

    #loginpage this appers first
    
def logon():
    l = tk.Tk()
    l.resizable(False,False)
    var = tk.StringVar()
    #l.geometry , settings
    l.title("Login")
    l.geometry('300x200')
    l.config(bg="Black")
    #actual code
    tk.Label(l, fg="White",bg="Black", text="Welcome to the injector").pack()
    tk.Label(l, fg="White",bg="Black", textvariable=var,foreground="Red").pack()
    tk.Label(l, fg="White",bg="Black", text="Enter credentials",pady=2).pack()
    tk.Label(l, fg="White",bg="Black", text="Username").pack()
    usr = tk.Entry(l,width=25)
    #PACKING ENTRIES IN A SEP. LINE SO IT WONT RETURN NaN
    usr.pack()
    tk.Label(l, fg="White",bg="Black", text="Password").pack()
    passw = tk.Entry(l,width=25)
    #PACKING ENTRIES IN A SEP. LINE SO IT WONT RETURN NaN
    passw.pack()
    def login():
            users = ['Marci','Cride']
            global usrn
            usrn = usr.get()
            if usrn in users:
                l.destroy()
                main()
                
            else:
                var.set("Wrong credentials!")
    #SUBMIT button, with verification
    tk.Button(l, text="Submit",command=login).pack(side=tk.BOTTOM)
    
    #l.destroy()
    l.mainloop()
#start login process
logon()