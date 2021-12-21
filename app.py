"""
Author:Savchenko Oleksii
Data: 02.2021
Update: 08.2021

"""

from sys import version_info
if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk
from tkinter import filedialog, Text, Label, Toplevel, Menu, messagebox
from time import *
import os


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(apps)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def openWin():
   global top
   top = Toplevel(root)
   Label(top, text=" Info ", font= ('Helvetica 14 bold')).pack()
   canvas = tk.Canvas(top, height=520, width=460, bg="#263D42", cursor='crosshair')
   canvas.pack(expand=False)

   frame = tk.Frame(top, bg="white")
   frame.place(relx=0.06, rely=0.10, relwidth=0.9, relheight=0.6)

   closeWin = tk.Button(top, text="Close", padx=35, fg='white', bg="#263D42",
   command=closeNewapps)
   closeWin.pack()
   top.grab_set()

def faqtxt():
    faq = tk.Tk()
    faq.title("Питання користувачів")
    txt_lbl="""Тренажер БПЛА - програмне забезпечення для навчання операторів.\n
    Підвищення кваліфікації та вдосконалення навичок операторів корисного навантаження."""
    labelExample = tk.Label(faq, justify=tk.LEFT, text=txt_lbl, height=10, width=80).pack(side="left")
    labelExample.pack()
    faq.mainloop()


def opentxt():
    app = tk.Tk()
    app.title("Про програму")
    txt_lbl="Тренажер для БПЛА\n Версія 0.8 beta"
    labelExample = tk.Label(app, text=txt_lbl, height=10, width=35)
    labelExample.pack()
    app.mainloop()

def runApps():
    for app in apps:
        os.startfile(app)


def closeApps():
    print("Window closed by customer")
    root.destroy()


def closeNewapps():
    print("PopWin closed by customer")
    top.destroy()


root = tk.Tk()
root.title('Тренажер БПЛА (beta version)')


mainmenu = Menu(root)
root.config(menu=mainmenu)


filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Запуск...", command=runApps)
filemenu.add_command(label="Відкрити файл", command=addApp)
filemenu.add_separator()
filemenu.add_command(label="Вихід", command=closeApps)

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="FAQ", command=faqtxt)
helpmenu.add_command(label="Про програму", command=opentxt)

mainmenu.add_cascade(label="Файл",
                     menu=filemenu)
mainmenu.add_cascade(label="Довідка",
                     menu=helpmenu)


root.iconphoto(False, tk.PhotoImage(file='sim.png'))
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        print(apps)


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(root, font=('calibri', 14, 'bold'),
            background='black',
            foreground='white')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='e')
time()


canvas = tk.Canvas(root, height=520, width=420, bg="#263D42", cursor='crosshair')
canvas.pack(expand=False)

frame = tk.Frame(root, bg="white")
frame.place(relx=0.06, rely=0.10, relwidth=0.9, relheight=0.6)


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()


with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
