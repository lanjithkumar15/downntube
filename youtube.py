import os
os.system('clear')print('-----------------------------------------------------------')
print('DOWNTUBE')
print('-----------------------------------------------------------------------------')
from pytube import YouTube
link=input("ENTER THE YOUTUBE LINK :")
yt = YouTube(link)
print("NEED 1 for VIDEO OR 2 for AUDIO")
vd = int(input("ENTER THE CHOICE :"))
if vd == 1:
    print("\n 0 for lowest resolution \n 1 for 360p resolution \n 2 for 720p resolution \n 3 for higher resolution")
    pixel =int(input("ENTER YOUR CHOICE :"))
    print("DOWNLOAD STARTED!!!!")
    if pixel == 0:
        db = yt.streams.get_lowest_resolution()
        db.download()
    elif pixel == 1:
        db = yt.streams.get_by_resolution("360p")
        db.download()
    elif pixel == 2:
        db = yt.streams.get_by_resolution("720p")
        db.download()
    elif pixel == 3:
        db = yt.streams.get_highest_resolution()
        db.download()
elif vd == 2:
    print("DOWNLOAD STARTED!!!!")
    df=yt.streams.get_audio_only()
    df.download()
    print("DONWLOAD COMPLETE!!!!")
    print("ENJOY!!!!")
else:
    print("ENTER A VALID INPUT")
    os.system('exit')

