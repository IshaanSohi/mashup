import streamlit as st
import os
st.title('Mashup')
st.write('Made by Singla saab')
name=st.text_input("Singer Name")
n=int(st.number_input("No. of videos"))
duration=int(st.number_input("duration of each video"))

#Email=st.text_input("Email id")
if st.button('Submit'):
    
        from youtube_search import YoutubeSearch
        results = YoutubeSearch(name, max_results=n).to_dict()
        link=['https://www.youtube.com/'+results[i]['url_suffix'] for i in range(n)]
        print(link)
        from pytube import YouTube
        def Download(link):
            youtubeObject = YouTube(link)
            youtubeObject = youtubeObject.streams.get_lowest_resolution()
            try:
                youtubeObject.download()
            except:
                print("An error has occurred")
            print("Download is completed successfully")

        for i in range(0,n):    
            Download(link[i])


        directory = 'C:\\Users\91700\Documents\Python'


        files = os.listdir(directory)


        mp4_files = [file for file in files if file.endswith('.mp4')]

        for file in mp4_files:
            print(file)

        print(mp4_files)

        from moviepy.editor import VideoFileClip,AudioFileClip

        for i in range(0,len(mp4_files)):
            video = VideoFileClip(mp4_files[i])
            audio = video.audio
            audio.write_audiofile("audio_file"+str(i)+".mp3")

        from pydub import AudioSegment

        import os
        #AudioSegment.converter = r"C:\Users\91700\Documents\Python\pyAI3.7\Scripts\ffmpeg.exe"
        #AudioSegment.ffmpeg = r"C:\Users\91700\Documents\Python\pyAI3.7\Scripts\ffmpeg.exe"
        #AudioSegment.ffprobe = r"C:\Users\91700\Documents\Python\pyAI3.7\Scripts\ffprobe.exe"

        directory = 'C:\\Users\91700\Documents\Python'

        files = os.listdir(directory)

        mp3_files = [file for file in files if file.endswith('.mp3')]

        for file in mp3_files:
            print(file)

        startMin = 0
        startSec = 00

        endMin = 0
#endSec = int(input('Enter time (in s)'))
#endSec=int(sys.argv[3])
        endSec=duration
        startTime = startMin*60*1000+startSec*1000
        endTime = endMin*60*1000+endSec*1000

        merger= AudioSegment.from_mp3(directory+str('\\')+mp3_files[0])
        merger=merger[0:0]
        for i in range(0,len(mp3_files)):
            song = AudioSegment.from_mp3(directory+str('\\')+mp3_files[i])
            extract = song[startTime:endTime] 
            merger+=extract
            extract.export( "audio_file_trim"+str(i)+'.mp3', format="mp3")
#name1=sys.argv[4]
        merger.export( "merged"+'.mp3', format="mp3")
#merger.export( name1, format="mp3")
        import zipfile 
        def compress_mp3_to_zip(mp3_file_path, zip_file_path):
            with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
                zip_file.write(mp3_file_path)

        compress_mp3_to_zip('merged.mp3', 'music.zip')

with open("music.zip", "rb") as fp:
    btn = st.download_button(
        label="Download ZIP",
        data=fp,
        file_name="merged.zip",
        mime="application/zip"
    )
