desc = '''Script making an audiofile taking first <dur> seconds of the songs of <artist>.

Usage: python mashup.py <artist> <num_vid> <dur> <outputFile>

This script searches for the songs of <artist> and take
<num_vid> videos' URLs, convert them to audio files and then
combine the first <dur> seconds of the audio into one 
single audio file with name <outputFile>.

The audio file will be saved in the <outputFile>.

'''

from pytube import *
import glob
import os
from pytube import *
import glob
import os
import urllib.request
import re
import pandas as pd
import random
from pytube import YouTube
from pydub import AudioSegment
import sys
import os
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText


try:
    artist = sys.argv[1]
    
    num_vid = int(sys.argv[2])
    
    dur = int(sys.argv[3])
    
    output_file = sys.argv[4]
except:
    print("Arguments missing.")
    print(desc)
    exit(-1)


artist=artist.lower()
artist=artist.replace(" ", "")+"videosongs"

html=urllib.request.urlopen("https://www.youtube.com/results?search_query="+artist)
video_ids=re.findall(r"watch\?v=(\S{11})" , html.read().decode())

l=len(video_ids)
url = []
for i in range(num_vid):
    str1 = "https://www.youtube.com/watch?v=" + video_ids[i]
    url.append(str1)

final_aud = AudioSegment.empty()

for i in range(num_vid):   
  audio = YouTube(url[i]).streams.filter(only_audio=True).first()
  audio.download(filename='file'+str(i)+'.mp3')
  
  aud_file = str(os.getcwd()) + '/file'+str(i)+'.mp3'
  file1 = AudioSegment.from_file(aud_file)
  
  extracted_file = file1[:dur*1000]
  final_aud +=extracted_file
  final_aud.export(output_file, format="mp3")

for i in range(num_vid):
    audio_f=aud_file = str(os.getcwd()) + '/file'+str(i)+'.mp3'
    os.remove(audio_f)

import shutil 
import os
from zipfile import ZipFile
import smtplib

path = str(os.getcwd())
path = path + "\\"
with ZipFile('mashup.zip', 'w') as zip_object:
    file_path = os.path.join(path + str(output_file)+".zip")
    zip_object.write(path + str(output_file), os.path.basename(path + str(output_file)))
