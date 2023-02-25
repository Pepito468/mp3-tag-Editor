# mp3-tag-Editor
Edit the tags of an mp3 file

Dependencies:
  mutagen (you can install it with 'pip install mutagen')

Command:
pyhon3 main.py [-h] [-t TITLE] [-ar ARTIST] [-al ALBUM] [-i IMAGE] filename

positional arguments:
  filename              Audio to be modified

options:
  -h, --help            show this help message and exit
  -t TITLE, --title TITLE
                        Set the new title for the mp3 file
  -ar ARTIST, --artist ARTIST
                        Set the new artist for the mp3 file
  -al ALBUM, --album ALBUM
                        Set the new album for the mp3 file
  -i IMAGE, --image IMAGE
                        Set the new image for the mp3 file. Keep in mind that your OS or your file manager might cache the old one, so you might need
                        to restart your machine to see any changes
