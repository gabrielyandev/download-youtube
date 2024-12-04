from cx_Freeze import setup, Executable
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("youtube_downloader_gui.py", base=base)]

setup(
    name = "YouTubeDownloader",
    version = "0.1",
    description = "YouTube Video Downloader",
    executables = executables
)
