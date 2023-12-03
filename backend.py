from pytube import YouTube

def download_video(link):
    try:
        url = link.get()
        YtObj = YouTube(url)
        video = YtObj.streams.get_highest_resolution()
        video.download()
        print("Download complete!")
    except:
        print("Youtube link is invalid")