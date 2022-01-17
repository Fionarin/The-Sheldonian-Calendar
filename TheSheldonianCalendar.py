from sqlite3 import Cursor
from tabnanny import check
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
from turtle import heading
from PIL import Image, ImageTk
from itertools import count, cycle
from tkinter.font import Font

from click import command
from gevent import config


Monday = "Thai Takeout Night"
Tuesday = "Cheesecake Factory Night"
Wednesday = "Halo Night & Comic Book Night"
Thursday = "Pizza Night"
Friday = "Chinese Takeaway & Vintage Game Night"
Saturday = "Laundry Night"
Sunday = "Sheldon Cooper does not have plans"
OPTIONS = (Wednesday, Tuesday, Sunday, Monday, Saturday, Friday, Thursday)


# Creating tkinter windows
window = tk.Tk()
window.title('The Sheldonian Calendar')
window.geometry('800x800')
window.configure(background='#eccf71')

frame = Frame(window, width=500, height=700, padx=20, pady=20)
frame.pack(padx=50, pady=100, ipadx=10, ipady=30)

hello = Label(window, text = "The Sheldonian Calendar", font=("Times", 30, BOLD), 
        background='#352839', fg='#ff562d', padx=13, pady=7)
hello.place(x=227, y=40)

welcome_label = Label(frame, text='''Dear Player,

        thank you for playing this game. I've created this game 
        in honor of Sheldon Cooper and his absurd rigit schedule.
        Let's see if you know, what Sheldon Cooper likes to do on
        a daily basis and figure out his weekly calendar.

Good luck!
        ''').pack()



# Monday
ttk.Label(frame, text = "Monday :",
        font = ("Arial", 16, BOLD)).pack()

n = tk.StringVar()
CBMonday = ttk.Combobox(frame, width = 27)
CBMonday.pack(side = TOP)

# Adding combobox drop down list
CBMonday['values'] =  OPTIONS
CBMonday.current(5)

# Tuesday
ttk.Label(frame, text = "Tuesday :",
        font = ("Arial", 16, BOLD)).pack()

n = tk.StringVar()
CBTuesday = ttk.Combobox(frame, width = 27)
CBTuesday.pack(side = TOP)

# Adding combobox drop down list
CBTuesday['values'] =  OPTIONS
CBTuesday.current(6)

# Wednesday

ttk.Label(frame, text = "Wednesday :",
        font = ("Arial", 16, BOLD)).pack()

n = tk.StringVar()
CBWednesday = ttk.Combobox(frame, width = 27)
CBWednesday.pack(side = TOP)

# Adding combobox drop down list
CBWednesday['values'] =  OPTIONS
CBWednesday.current(0)

# Thursday

ttk.Label(frame, text = "Thursday :",
        font = ("Arial", 16, BOLD)).pack()

n = tk.StringVar()
CBThursday = ttk.Combobox(frame, width = 27)
CBThursday.pack(side = TOP)

# Adding combobox drop down list
CBThursday['values'] =  OPTIONS
CBThursday.current(2)

# Friday

ttk.Label(frame, text = "Friday :",
        font = ("Arial", 16, BOLD)).pack()

n = tk.StringVar()
CBFriday = ttk.Combobox(frame, width = 27)
CBFriday.pack(side = TOP)

# Adding combobox drop down list
CBFriday['values'] =  OPTIONS
CBFriday.current(4)

# Saturday

ttk.Label(frame, text = "Saturday :",
        font = ("Arial", 16, BOLD)).pack()

n = tk.StringVar()
CBSaturday = ttk.Combobox(frame, width = 27)
CBSaturday.pack(side = TOP)

# Adding combobox drop down list
CBSaturday['values'] =  OPTIONS
CBSaturday.current(3)

# Sunday

ttk.Label(frame, text = "Sunday :",
        font = ("Arial", 16, BOLD)).pack()

n = tk.StringVar()
CBSunday = ttk.Combobox(frame, width = 27)
CBSunday.pack(side = TOP)

# Adding combobox drop down list
CBSunday['values'] =  OPTIONS
CBSunday.current(1)

class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
 
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
 
# function to open a new window
# on a button click
def openNewWindow(richtig_falsch):
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)
    newWindow.title("Your Answer")
    newWindow.geometry("600x500")
    newWindow.configure(background='#352839')
 
    # A Label widget to show in toplevel
    myLable = Label(newWindow, text = richtig_falsch, font=("Arial", 30), 
        background='#352839', fg='#eccf71')
    myLable.place(x=80, y=50)

    if richtig_falsch == "Well look at that, you got it right!":
            myImage = ImageLabel(newWindow)
            myImage.load("Correct.gif")
            myImage.place(x=85, y=100)
    elif richtig_falsch == "             You are wrong!":
            image_wrong = ImageTk.PhotoImage(Image.open("Bazinga.jpg"))
            myImage1 = Label(newWindow, image=image_wrong)
            myImage1.image = image_wrong
            myImage1.place(x=150, y=100)

def Check():
        if(CBMonday.get() == Monday and CBTuesday.get() == Tuesday and 
            CBWednesday.get() == Wednesday and CBThursday.get() == Thursday and
            CBFriday.get() == Friday and CBSaturday.get() == Saturday and 
            CBSunday.get() == Sunday):
            richtig_falsch = "Well look at that, you got it right!"
        else:
            richtig_falsch = "             You are wrong!"
        openNewWindow(richtig_falsch)

myButton = Button(frame, text = "Check Answers", command=Check)
myButton.pack(side='bottom', padx='5', pady='20')

window.mainloop()