# You can get all the info if you watch the videos I uploaded in YouTube
# just search typical computer guy and click the first channel ... go to the python playlist and you will find useful projects like this one


# importing required modules
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


# this function creates and defines all the properties of all the buttons, text boxes, etc.
def Widgets():
	head_label = Label(root, text="YT Video Downloader",
					padx=15,
					pady=15,
					font="callibri",
					bg="white",
					fg="red")
	head_label.grid(row=1,
					column=1,
					pady=10,
					padx=5,
					columnspan=3)

	link_label = Label(root,
					text="URL: ",
					bg="pink",
					pady=5,
					padx=5)
	link_label.grid(row=2,
					column=0,
					pady=5,
					padx=5)

	root.linkText = Entry(root,
						width=35,
						textvariable=video_Link,
						font="callibri")
	root.linkText.grid(row=2,
					column=1,
					pady=5,
					padx=5,
					columnspan=2)


	destination_label = Label(root,
							text="Save in ",
							bg="pink",
							pady=5,
							padx=9)
	destination_label.grid(row=3,
						column=0,
						pady=5,
						padx=5)


	root.destinationText = Entry(root,
								width=27,
								textvariable=download_Path,
								font="callibri")
	root.destinationText.grid(row=3,
							column=1,
							pady=5,
							padx=5)


	browse_B = Button(root,
					text="Browse",
					command=Browse,
					width=10,
					bg="orange",
					relief=GROOVE)
	browse_B.grid(row=3,
				column=2,
				pady=1,
				padx=1)

	Download_B = Button(root,
						text="Download",
						command=Download,
						width=20,
						bg="black",
						fg="white",
						pady=10,
						padx=15,
						relief=GROOVE,
						font="callibri")
	Download_B.grid(row=4,
					column=1,
					pady=20,
					padx=20)


# function to open a dialog box and browse to the save location (directory)
def Browse():
	download_Directory = filedialog.askdirectory(
		initialdir="Path:", title="Save Video")
	download_Path.set(download_Directory)

# function to download the video
def Download():
	Youtube_link = video_Link.get()
	download_Folder = download_Path.get()
	getVideo = YouTube(Youtube_link)
	videoStream = getVideo.streams.get_highest_resolution()
	videoStream.download(download_Folder)
	messagebox.showinfo("Success","Video Downloaded")


root = tk.Tk()
root.geometry("520x280")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="white")
video_Link = StringVar()
download_Path = StringVar()
Widgets()
root.mainloop()
