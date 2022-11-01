import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as font
import sys

def App():
    def Screen1():
        root = tk.Tk()
        root.title("Splash Screen")
        root.geometry("1165x600+5+5")
        root.resizable(False, False)
        #font
        myFont = font.Font(size=12, family='Courier')
        #Splash Screen
        my_img2 = ImageTk.PhotoImage(Image.open("C:\\Users\\4229800\\Documents\\App_Challenge\\images\\Splash_logo.png"))
        background_label = tk.Label(root, image = my_img2)
        background_label.place(x = 0, y = 0)
        #nextbutton
        btn = Button(root, text = 'Click To Proceed', bg='#6c7175', fg='white', bd = '2', height=2, width=110, command = root.destroy)
        btn ['font'] = myFont
        btn.place(x=20, y=10)
        #endbutton
        btn = Button(root, text = 'End Entire Program', bg='#3d4142', fg='white', bd = '2', height=1, width=20, command = sys.exit)
        btn ['font'] = myFont
        btn.place(x=470, y=70)
        root.mainloop()
    Screen1()
   
    def Screen2():
        root = Tk()
        root.title('Main Page')
        root.geometry('500x600+150+25')
        root.resizable(False, False)
        root['bg']='#384c6c'
        mF = font.Font(size=20, family= 'Courier', weight='bold')
        myFont = font.Font(size=13, family='Courier')
        text = Text(root, width= 80, height= 1, background= "#384c6c", bd='0', fg="white",font= mF)
        text.insert(INSERT, "Welcome to Key Master!")
        text.place(x=5, y=5)
        text = Text(root, width= 48, height= 4, background= "#384c6c", bd='0', fg="white",font= myFont)
        text.insert(INSERT, "This program is designed to help people navigate and understand their computer more.\n It will help you understand the concecpt of \n'Key Master'")
        text.place(x=5, y=40)
        text = Text(root, width= 100, height= 1, background= "#384c6c", bd='0', fg="white",font= myFont)
        text.insert(INSERT, "Please Proceed by clicking on 'Daily Lesson'")
        text.place(x=5, y=120)
        btn = Button(root, text = 'Daily Lesson', bd = '3', bg='#6c7175', fg='white', height=1, width=48, command = root.destroy)
        btn ['font'] = myFont
        btn.place(x=5, y=515)
        image = Image.open("C:\\Users\\4229800\\Documents\\App_Challenge\\pc.png")
        resize_image = image.resize((300, 300))
        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(image=img)
        label1.image = img
        label1.place(x=100, y=150)
        btn = Button(root, text = "Quit Program", bd = '3', bg='#3d4142', fg='white', height=1, width=48, command = sys.exit)
        btn ['font'] = myFont
        btn.place(x=4, y=560)
        root.mainloop()
    Screen2()

    def Screen3():      
        root = Tk()
        root.title('Daily Lesson')
        root.geometry('500x600+150+25')
        root.resizable(False, False)
        root.configure(bg='#384c6c')
        myFont = font.Font(size=13, family='Courier')
        bold = font.Font(size=13, family='Courier', weight="bold", slant="italic")
        text = Text(root, width= 55, height= 3, background= "#384c6c", bd='0', fg="white",font= myFont)
        text.insert(INSERT, "Here are some basic Hotkeys to learn \nusing your Keyboard!")
        text.place(x=5, y=50)
        btn = Button(root, text = "Return To Main Page", bd = '3', bg='#6c7175', fg='white', command = root.destroy)
        btn ['font'] = myFont
        btn.place(x=150, y=5)
        text = Text(root, width= 55, height= 3, background= "#384c6c", bd='0', fg="white",font= myFont)
        text.insert(INSERT, "• Ctrl C allows you to copy a higlighted area \nwhile Ctrl V allows you to paste what you copied")
        text.place(x=5, y=95)
        text = Text(root, width= 48, height= 4, background= "#384c6c", bd='0', fg="white",font= bold)
        text.insert(INSERT, "• To change the style of text you can press Ctrl I or B \nCtrl I will Italisize your text while \nCtrl B will make it Bold")
        text.place(x=5, y=140)
        text = Text(root, width= 48, height= 4, background= "#384c6c", bd='0', fg="white",font= myFont)
        text.insert(INSERT, "• Windows key + d will show you your desktop")
        text.place(x=5, y=220)
        text = Text(root, width= 48, height= 4, background= "#384c6c", bd='0', fg="white",font= myFont)
        text.insert(INSERT, "• Ctrl + F will open a search bar allowing you \nto find something by typing in characters")
        text.place(x=5, y=255)
        text = Text(root, width= 48, height= 4, background= "#384c6c", bd='0', fg="white",font= myFont)
        text.insert(INSERT, "• Alt + Shift + S will take a screenshot")
        text.place(x=5, y=300)
        image = Image.open("C:\\Users\\4229800\\Documents\\App_Challenge\\screenshot_ex.png")
        resize_image = image.resize((450, 150))
        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(image=img)
        label1.image = img
        label1.place(x=5, y=332)
        text = Text(root, width= 48, height= 4, background= "#384c6c", bd='0', fg="white",font= myFont)
        text.insert(INSERT, "• Windows Button + L will lock your computer,\n useful for when you're away from your computer")
        text.place(x=5, y=500)
        #btn = Button(root, text = "End Program", bd = '4', height=1, width=48, bg='#3d4142', fg='white', command = sys.exit)
        #btn.place(x=4, y=560)
        root.mainloop()
    Screen3()
    
    def hs():
        root = Tk()
        root.title('Main Page')
        root.geometry('500x600+150+25')
        root.resizable(False, False)
        #root.configure(bg='#87CEEB')
        root.configure(bg='#384c6c')
        mF = font.Font(size=20, family= 'Courier', weight='bold')
        myFont = font.Font(size=13, family='Courier')
        text = Text(root, width= 80, height= 1, background= "#384c6c", bd='0', fg="white",font= mF)
        text.insert(INSERT, "Welcome to Key Master!")
        text.place(x=5, y=5)
        text = Text(root, width= 48, height= 4, background= "#384c6c", bd='0', fg="white",font= myFont)
        text.insert(INSERT, "This program is designed to help people navigate and understand their computer more.\n It will help you understand the concecpt of \n'Key Master'")
        text.place(x=5, y=40)
        text = Text(root, width= 100, height= 1, background= "#384c6c", bd='0', fg="white",font= myFont)
        text.insert(INSERT, "Please Proceed by clicking on 'New Tips'")
        text.place(x=5, y=120)
        #btn = Button(root, text = 'Daily Lesson', bd = '3', bg='#6c7175', fg='white', height=1, width=48, command = root.destroy)
        #btn ['font'] = myFont
        #btn.place(x=5, y=515)
        image = Image.open("C:\\Users\\4229800\\Documents\\App_Challenge\\pc.png")
        resize_image = image.resize((300, 300))
        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(image=img)
        label1.image = img
        label1.place(x=100, y=150)
        btn = Button(root, text = 'New Tips', bd = '3', bg='#6c7175', fg='white', height=1, width=48, command = root.destroy)
        btn ['font'] = myFont
        btn.place(x=5, y=558)
        #btn = Button(root, text = "Quit Program", bd = '3', bg='#3d4142', fg='white', height=1, width=48, command = sys.exit)
        #btn ['font'] = myFont
        #btn.place(x=4, y=560)
        root.mainloop()
    hs()
    
    def S3():      
        root = Tk()
        root.title('New Tips')
        root.geometry('500x600+150+25')
        root.resizable(False, False)
        root.configure(bg='#384c6c')
        myFont = font.Font(size=12, family='Courier')
        text = Text(root, width= 55, height= 3, background= "#384c6c", bd='0', fg="white",font= myFont)
        text.insert(INSERT, "Here are some handy tricks to learn \nfor using your computer!")
        text.place(x=5, y=50)
        btn = Button(root, text = "Continue To Final Page", height=1, width=48, bd = '3', bg='#6c7175', fg='white', command = root.destroy)
        btn ['font'] = myFont
        btn.place(x=4, y=5)
        text = Text(root, width= 55, height= 3, background= "#384c6c", bd='0', fg="white",font= myFont)
        text.insert(INSERT, "• When you go to open your browser such as Google or \nInternet, pressing Ctrl + Shift + T will \nrestore your pages")
        text.place(x=5, y=95)
        image = Image.open("C:\\Users\\4229800\\Documents\\App_Challenge\\restore_tabs.png")
        resize_image = image.resize((450, 150))
        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(image=img)
        label1.image = img
        label1.place(x=5, y=150)
        text = Text(root, width= 48, height= 4, background= "#384c6c", bd='0', fg="white",font= myFont)
        text.insert(INSERT, "• To close any screen on your computer you can \nsimply press the 'X' at the top right corner or \npress ALT + F4")
        text.place(x=5, y=320)
        image = Image.open("C:\\Users\\4229800\\Documents\\App_Challenge\\alt_f4.png")
        resize_image = image.resize((450, 150))
        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(image=img)
        label1.image = img
        label1.place(x=5, y=400)
        #text = Text(root, width= 48, height= 4, background= "#384c6c", bd='0', fg="white",font= myFont)
        #text.insert(INSERT, "• Windows key + d will show you your desktop")
        #text.place(x=5, y=230)
        #text = Text(root, width= 48, height= 4, background= "#384c6c", bd='0', fg="white",font= myFont)
        #text.insert(INSERT, "• Ctrl + F will open a search bar allowing you \nto find something by typing in characters")
        #text.place(x=5, y=265)
        #text = Text(root, width= 48, height= 4, background= "#384c6c", bd='0', fg="white",font= myFont)
        #text.insert(INSERT, "• Alt + Shift + S will take a screenshot")
        #text.place(x=5, y=310)
        #text = Text(root, width= 48, height= 4, background= "#384c6c", bd='0', fg="white",font= myFont)
        #text.insert(INSERT, "• Windows Button + L will lock your computer,\n useful for when you're away from your computer")
        #text.place(x=5, y=350)
        root.mainloop()
    S3()
    

    
    def last():
        root = Tk()
        root.title('Final Page')
        root.geometry('500x600+150+25')
        root.resizable(False, False)
        #root.configure(bg='#87CEEB')
        root.configure(bg='#384c6c')
        mF = font.Font(size=15, family= 'Courier', weight='bold')
        myFont = font.Font(size=14, family='Courier')
        text = Text(root, width= 100, height= 1, background= "#384c6c", bd='0', fg="white",font= mF)
        text.insert(INSERT, "Thanks for using Key Master!")
        text.place(x=5, y=5)
        text = Text(root, width= 48, height= 3, background= "#384c6c", bd='0', fg="white",font= myFont)
        text.insert(INSERT, "We hope to see you soon!")
        text.place(x=5, y=40)
        text = Text(root, width= 100, height= 3, background= "#384c6c", bd='0', fg="white",font= myFont)
        text.insert(INSERT, "Please Exit by pressing the 'Finish Program' \nbutton below")
        text.place(x=5, y=80)
        btn = Button(root, text = 'Finish Program', bd = '2', bg='#6c7175', fg='white', height=2, width=43, command = root.destroy)
        btn ['font'] = myFont
        btn.place(x=9, y=535)
        root.mainloop()
    last()
    
App()
