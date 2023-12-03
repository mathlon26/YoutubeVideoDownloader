import tkinter
import customtkinter as ctk
from pytube import YouTube
from PIL import Image, ImageTk
from urllib.request import urlopen
completion_percentage = 0.0
percentage_text = "0%"

img = Image.Image()

def download_video():
    try:
        if (ctk.get_appearance_mode() == "light"):
            color = "white"
        else:
            color = "black"
            
        finish_label.configure(text="Downloading...")
        finish_label.update()
        
        url = link.get()
        YtObj = YouTube(url, on_progress_callback=on_progress)
        img = Image.Image(urlopen(YtObj.thumbnail_url).read())
        video_thumbnail.configure(image=img)
        
        video_title.configure(text=YtObj.title)
        video_title.update()
        video_channel.configure(text=YtObj.channel_id)
        video_channel.update()
        video_description.configure(text=YtObj.description)
        video_description.update()
        video_views.configure(text=YtObj.views)
        video_views.update()
        video_length.configure(text=str(YtObj.length/60))
        video_length.update()
        
        video = YtObj.streams.get_lowest_resolution()

        title.configure(text=YtObj.title, text_color=color)
        title.update()

        video.download()
        
        finish_label.configure(text="Download complete")
        finish_label.update()
        
    except:
        finish_label.configure(text="Download Error", text_color="red")
        finish_label.update()
        

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    completion_percentage = bytes_downloaded / total_size* 100
    percentage_text = str(int(completion_percentage))
    progress_percentage.configure(text=percentage_text + "%")
    progress_percentage.update()
    
    progress_bar.set(0.2 + float(completion_percentage)/100)


# System settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# App frame
app = ctk.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI elements
title = ctk.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = ctk.CTkEntry(app, width=350, height=40, placeholder_text="YouTube URL ...", textvariable=url_var)
link.pack()

# Download finished
finish_label = ctk.CTkLabel(app, text="")
finish_label.pack()

# Progress percentage
progress_percentage = ctk.CTkLabel(app, text="0%")
progress_percentage.pack(padx=10, pady=10)

progress_bar = ctk.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Submit input
download = ctk.CTkButton(app, text="Download", command=download_video)
download.pack(padx=10, pady=10)

# Info
video_thumbnail = ctk.CTkImage(light_image=img, dark_image=img)

video_title = ctk.CTkLabel(app, text="")
video_title.pack()
video_views = ctk.CTkLabel(app, text="")
video_views.pack()
video_description = ctk.CTkLabel(app, text="")
video_description.pack()
video_length = ctk.CTkLabel(app, text="")
video_length.pack()
video_channel = ctk.CTkLabel(app, text="")
video_channel.pack()


# Run app
app.mainloop()