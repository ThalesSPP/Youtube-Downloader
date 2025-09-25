from pytubefix import Playlist
from pytubefix.cli import on_progress

url = "url"

finalPath = "path"

pl = Playlist(url)
for video in pl.videos:
    ys = video.streams.get_audio_only()
    ys.download(output_path=finalPath)
