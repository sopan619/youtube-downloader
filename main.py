from pytube import YouTube

# Takes youtube link input here
link=input("Paste your link here : ")
# passing it to YouTube class 
yt =YouTube(link)
# Getting video title 
title = yt.title
# Taking desired resolution input from user
reso= input("Enter Download Quality [144p, 240p, 360p, 480p, 720p, 1080p, 1440p or 2160p] = ")
# A warning statement
print("Note, if the entered quality is not available, the program won't work. Try with lower quality.")

# Getting that video stream
vid = yt.streams.filter(res=reso)
# print(vid)
print("The Video is being downloaded, kindly wait...")

# Getting audio stream
aud = yt.streams.filter(only_audio=True)
# print(aud)

# Downloading the files 
vid.first().download('Downloads/Video')
aud.last().download('Downloads/Audio')

# Download complete message 
print("\nTitle : ", title )
print('Download is completed. Merge the Audio and Video file together.\n')
