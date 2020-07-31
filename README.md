# video_download
video_download (youtube, streaming videos)


First you need ffmpeg definitely.
ffmpeg 다운로드(download)
1. Download ffmpeg in https://ffmpeg.org/download.html
2. Unzip ffmpeg~.zip file
3. Enter in bin and copy ffmpeg.exe to directory which has youtube-dl.exe
4. Now you can use youtube-dl.exe completely

Now, you can download youtube video, youtube_channel, youtube_playlist and streaming videos (like TWITCH TV, AfreecaTV, huya.com and else..).


How to use:

1. pip install -r requiremnets.txt

2. In terminal, Go to the directory with general.py

3. Input the command
  if you want youtube_download:
   
   python general.py youtube --url "youtube_video or youtube_channel or playlist url" --name "download directory 
                                                                                              (defalut= video - current directory / youtube_channel or playlist - title)
    - YOUTUBE VIDEO -
    ex) python general.py youtube --url https://www.youtube.com/watch?v=TgOu00Mf3kI --name IU
    => new directory "IU" is created and download IU video in directory "IU"

    - YOUTUBE CHANNEL -
    ex) python general.py youtube --url https://www.youtube.com/user/JFlaMusic
    => url is JFlaMusic channel and new directory is created with name "JFlaMusic" which is the title of the channel and download all videos of the channel in directory "JFlaMusic"

    - YOUTUBE PLAYLIST -
    ex) python general.py youtube --url https://www.youtube.com/playlist?list=PL4C2OaC1jQqR3ICDBf4j1dH1Fk4uIo-Lx
    => url is JFlaMusic cover playlist and new directory is created with name "cover" which is the title of the playlist and download all videos of the channel in directory "cover"
  
  
  if you want stream_download:
  
   python general.py stream --url "stream url" --name "file_name"

    - TWITCH TV -
    ex) python general.py stream --url https://www.twitch.tv/leehunnyeo --name luda (default - streamer id)
    
    - afreecatv -
    ex) python general.py stream --url http://play.afreecatv.com/pi0314/225784567 --name 
    => url is stream url and make directory with name "bj_name" and download option name or if you don't insert name, content is name.
    
    - huya.com -
    ex) python general.py stream --url http://huya.com/en777 --name 
    => url is stream url and make directory with name "host_name" and download option name or if you don't insert name, content is name.
