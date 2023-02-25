#Libs
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, APIC
import argparse
import os

###Scrypt

#Arguments for Terminal
commands = argparse.ArgumentParser(description = "Modify properties of an mp3 file")
commands.add_argument("filename",type = str, help="Audio to be modified") #must be provided
commands.add_argument("-t","--title",type = str, help = "Set the new title for the mp3 file")
commands.add_argument("-ar","--artist",type = str, help = "Set the new artist for the mp3 file")
commands.add_argument("-al","--album",type = str, help = "Set the new album for the mp3 file")
commands.add_argument("-i","--image",type = str, help = "Set the new image for the mp3 file. Keep in mind that your OS or your file manager might cache the old one, so you might need to restart your machine to see any changes")
args = commands.parse_args()

#Audio modifier

if not os.path.exists(args.filename):
    #Error in input name
    print("No such file")
else:
    #Start the thing
    audio = MP3(args.filename)

    if not audio.tags:
        audio.add_tags()
    
    tags = audio.tags

    #Modify tags
    if args.title:
        if "TIT2" in tags:
            del tags["TIT2"]
        tags.add(TIT2(encoding=3, text=args.title))
    if args.artist:
        if "TPE1" in tags:
            del tags["TPE1"]
        tags.add(TPE1(encoding=3, text=args.artist))
    if args.album:
        if "TALB" in tags:
            del tags["TALB"]
        tags.add(TALB(encoding=3, text=args.album))
    if args.image:
        if "APIC:" in tags:
            del tags["APIC:"]
        try:
            tags.add(APIC(encoding=3, mime="image/jpeg", type=3, desc=u"Cover", data=open(args.image,"rb").read()))
        except FileNotFoundError:
            print("Image file not found")

    tags.save(args.filename)
    audio.save(args.filename)