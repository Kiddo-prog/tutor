import tkinter
from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("500x500")
root.title("Youtube downloader app")

Label(root, text='Youtube Downloader App', font='serif 10 bold').pack()

link = StringVar()

Label(root, text='Paste your link here: ')


root.mainloop