# apt-get install python-tk
# pip install tk
# pip install customtkinter
# python -m pip install pytube
# python -m pip install git+https://github.com/pytube/pytube
#

import tkinter 
import customtkinter
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable, PytubeError


# add directory button change driectory
'''from tkinter import filedialog
from tkinter import *
import glob, os, shutil

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

def set_dir():
    sourcePath = str(folder_path)
    os.chdir(sourcePath)  # Provide the path here

root = customtkinter.CTk()
folder_path = StringVar()

lbl1 = customtkinter.CTkLabel(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)

buttonBrowse = Button(text="Browse folder", command=browse_button)
buttonBrowse.grid(row=2, column=1)
buttonSetDir = Button(root, text='Set directory', command=set_dir).grid(row=2, column=2, sticky=W, pady=4)
#mainloop()'''

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.filter(progressive=True, file_extension='mp4').first().download()
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        if video:
            #video.download()
            #print("Download Completed")
            finishLabel.configure(text="Downloaded!", text_color="green")
        else:
            finishLabel.configure(text="No video found with the specified parameters", text_color="red")
            print("No video found with the specified parameters")
    #except RegexMatchError:
    #    print("Invalid YouTube URL provided")
    #   finishLabel.configure(text="Invalid YouTube URL provided", text_color="red")
    except VideoUnavailable:
        print("The video is unavailable, restricted, or a bad link")
        finishLabel.configure(text="The video is unavailable, restricted, or a bad link", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completeion = bytes_downloaded / total_size * 100
    #print(percentage_of_completeion)
    per = str(int(percentage_of_completeion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    # Update progress bar
    progressBar.set(float(percentage_of_completeion) / 100)



# System Setting
#customtkinter.set_appearance_mode("dark")
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a Youtube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)


# Downlaod Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()
 
