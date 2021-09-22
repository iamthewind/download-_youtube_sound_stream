from pytube import YouTube
import sys

url_to_download = "https://www.youtube.com/watch?v=IE8oV15nMVk"

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 
    percentage_of_completion = int(bytes_downloaded / total_size * 100 / 5)
    sys.stdout.write('\r')
    sys.stdout.write("[%-20s] %d%%" % ('='*percentage_of_completion, 5*percentage_of_completion))
    sys.stdout.flush()

yt = YouTube(url=url_to_download,on_progress_callback=on_progress)
stream = yt.streams.get_audio_only()
stream.download()