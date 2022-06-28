from tkinter import *
from tkinter.ttk import *

from time import strftime
#https://www.youtube.com/watch?v=at7rpdT8FeI
root = Tk()
root.title("Clock")

def time():
    string = strftime("%I:%M:%S %p")
    label.config(text = string)
    label.after(1000, time)

label = Label(root, font = "ds-digital 100", background = "black", foreground = "red")
label.pack(anchor = "center")

time()

mainloop()