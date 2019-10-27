#youtube audio download
'''
to download to iphone:
    1) connect iphone to computer iTunes
    2) in Songs, File>Add File to Library
    2) click little phone icon at top left
    3) Go to Music
    4) check Sync Music
'''


from __future__ import unicode_literals
#yt download
import youtube_dl
#file manipulation
import os
#command line tool
from sys import argv

#python dict for youtube library download configurations
dlconfigs = {
        #get best format for audio
        'format': 'bestaudio/best',
        #filename is variable
        'outtmpl':'%(title)s.%(ext)s',
        #dont check certificate
        'nocheckcertificate': True,
        #after video is downloaded
        'postprocessors': [{
                #use FFmpeg to extract audio
                'key': 'FFmpegExtractAudio',
                #encode as mp3
                'preferredcodec': 'mp3',
                #preferred quality
                'preferredquality': '192',
        }]
}
        
#make dir for downloaded mp3 if not there
if not os.path.exists('YoutubeSongs'):
    os.mkdir('YoutubeSongs')
    #otherwise just go to YoutubeSongs
else:
    os.chdir('YoutubeSongs')

#downloading songs
    #creating youtube_dl class as dl
with youtube_dl.YoutubeDL(dlconfigs) as dl:
    with open('../' + argv[1], 'r') as f:
        for url in f:
            dl.download([url])