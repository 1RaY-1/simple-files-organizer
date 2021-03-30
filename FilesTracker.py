""" Before you start using it, you need to enter your username and change directories if needed """

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time
import shutil

### CONFIGURE ###
user = "" ### ENTER YOUR USERNAME HERE

# the main folder to track
folder_track = "/home/" + user + "/Downloads"

# all possible folder destinations
image_folder = "/home/" + user + "/Downloads/Photos"
video_folder = "/home/" + user + "/Downloads/Videos"
music_folder = "/home/" + user + "/Downloads/Music"
web_folder = "/home/" + user + "/Downloads/Web"
compressed_folder = "/home/" + user + "/Downloads/Compressed"
development_folder = "/home/" + user + "/Downloads/Development"
else_folder = "/home/" + user + "/Downloads/Else"

# this is for the last condition, in this  case it's just working like else, but we don't need else, because it will ruin everything
all_extensions = ['jpg', 'jpeg', 'png', 'gif', 'html', 'css', 'm4a', 'mp3',
'flac', 'wav', 'mp4', 'webm', 'mov', 'zip', 'rar', '7z', 'tar',
'c', 'cpp', 'py', 'cs', 'js', 'sh']

class Handler(FileSystemEventHandler):

    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extension = filename.split(".")

            """ check files """
            file = folder_track + "/" + filename

#           check for images
            if len(extension) > 1 and (extension[1].lower() == "jpg" or extension[1].lower() == "jpeg" or extension[1].lower() == "png" or extension[1].lower() == "gif"):
                dest_dir = image_folder + "/" # for this file extensions this is the destination directory
#               if needed directory does not exist, program will create it
                if os.path.isdir(dest_dir) == False:
                    os.mkdir(dest_dir)
#               finally move the file to it's the destination directory
                shutil.move(file, dest_dir)

#           and repeat the same operation for each file extension

#           check for web (html, css)
            elif len(extension) > 1 and (extension[1].lower() == "html" or extension[1].lower() == "css"):
                dest_dir = web_folder + "/"
                if os.path.isdir(dest_dir) == False:
                    os.mkdir(dest_dir)
                shutil.move(file, dest_dir)

#           check for music
            elif len(extension) > 1 and (extension[1].lower() == "m4a" or extension[1].lower() == "mp3" or extension[1].lower() == "flac" or extension[1].lower() == "wav"):
                dest_dir = music_folder + "/"
                if os.path.isdir(dest_dir) == False:
                    os.mkdir(dest_dir)
                shutil.move(file, dest_dir)

#           check for videos
            elif len(extension) > 1 and (extension[1].lower() == "mp4" or extension[1].lower() == "webm" or extension[1].lower() == "mov"):
                dest_dir = video_folder + "/"
                if os.path.isdir(dest_dir) == False:
                    os.mkdir(dest_dir)
                shutil.move(file, dest_dir)

#           check for compressed files
            elif len(extension) > 1 and (extension[1].lower() == "zip" or extension[1].lower() == "rar" or extension[1].lower() == "7z" or extension[1].lower() == "tar"):
                dest_dir = compressed_folder + "/"
                if os.path.isdir(dest_dir) == False:
                    os.mkdir(dest_dir)
                shutil.move(file, dest_dir)

#            check for some programming languages 
            elif len(extension) > 1 and (extension[1].lower() == "c" or extension[1].lower() == "cpp" or extension[1].lower() == "py" or extension[1].lower() == "cs" or extension[1].lower() == "js" or extension[1].lower() == "sh"):
                dest_dir = development_folder + "/"
                if os.path.isdir(dest_dir) == False:
                    os.mkdir(dest_dir)
                shutil.move(file, dest_dir)
            
#           if none of this extensions, it is like else
            elif len(extension) > 1 and (extension[1].lower() != all_extensions):
                dest_dir = else_folder + "/"
                if os.path.isdir(dest_dir) == False:
                    os.mkdir(dest_dir)
                shutil.move(file, dest_dir)
            
# run
if __name__ == '__main__':

    handle = Handler()
    observer = Observer()
    observer.schedule(handle, folder_track, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
