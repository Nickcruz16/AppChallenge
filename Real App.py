import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

def Screen1():
    root = Tk()
    root.title('Test')
    root.state('zoomed')
    bg = PhotoImage(file = "dog.jpg")
    canvas1 = Canvas(root, width=400,height=400)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image(0,0,image = bg, anchor = "nw")
    
    #image1 = Image.open("C:\\Users\\4229800\\Downloads\\startingScreen.png")
    #image1.thumbnail((1000,1000))    
    #test = ImageTk.PhotoImage(image1)
    #label1 = tkinter.Label(image=test)
    #label1.image = test
    #label1.place(x=0, y=0)
    btn = Button(root, text = 'Click To Proceed', bd = '5', command = root.destroy)
    btn.pack(side = 'top')
    btn = Button(root, text = 'Die', bd = '5', command = root.destroy)
    btn.pack(side = 'bottom')
    root.mainloop()
Screen1()

def Screen2():
    root = Tk()
    root.title('Example of New Screen')
    root.state('zoomed')
    btn = Button(root, text = 'Next Page', bd = '5', command = root.destroy)
    btn.pack(side = 'top')
    btn = Button(root, text = 'Die', bd = '5', command = root.destroy)
    btn.pack(side = 'bottom')
    btn = Button(root, text = "go back", bd = '5', command = Screen1)
    btn.pack(side = 'right')
    root.mainloop()
Screen2()

def Screen3():
    root = Tk()
    root.title('Last Screen')
    root.state('zoomed')
    btn = Button(root, text = 'Next Page (4)', bd = '5', command = root.destroy)
    btn.pack(side = 'top')
    btn = Button(root, text = "go back", bd = '5', command = Screen2)
    btn.pack(side = 'right')
    root.mainloop()
Screen3()
