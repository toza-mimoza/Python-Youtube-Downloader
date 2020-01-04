import pafy
import sys


def download_video(url, path, music=False):
        
    try:
        #make a new pafy object
        vid=pafy.new(url,gdata=True,size=True)
    
    except:
        #needs exception handling if the link is really invalid 
        print("The link is invalid.")
        sys.exit(1)

    if music==True: #only audio stream is considered
        #get the list of all audio streams and print it
        audio_streams=vid.audiostreams
        print(audio_streams)
        
        #print the information about the audio stream 
        for audiostream in audio_streams:
            print("audio stream: ")
            extension=audiostream.extension
            print(extension)
            bitrate=audiostream.bitrate
            print(bitrate)
            filesize=audiostream.get_filesize()
            filesize_MB=round((filesize/1024)/1024,2)
            print("Size is "+str(filesize)+" bytes ("+str(filesize_MB)+" MB)")

            if audiostream.extension=='m4a': # if the audio stream is in m4a format, download it 
                
                audiostream.download(path)
                pass
        pass
    
    else:

        #find the best video stream
        best_stream=vid.getbest()

        #print video metadata
        print(vid)

        #get the size of the video
        filesize=best_stream.get_filesize()

        #get the video format
        extension=best_stream.extension

        #get the video resolution
        resolution=best_stream.resolution

        #print file format
        print("File format: "+str(extension))

        #print resolution
        print("Video resolution: "+str(resolution))

        #calculater file size in MB and print it 
        filesize_MB=round((filesize/1024)/1024,2)
        print("Size is "+str(filesize)+" bytes ("+str(filesize_MB)+" MB)")

        #donwload the best quality video format
        filename=best_stream.download(path)

def download_playlist(url, path, music=False):
    try:
        pl=pafy.get_playlist(url) # make a Pafy object
    
    except:
        print("The link is invalid.")
        sys.exit(1)

    #loop through each video and download it 
    for i in range(len(pl['items'])):
        #the pafy object of a video in the playlist is under 'pafy' 
        vid=pl['items'][i]['pafy']
        # print video metadata
        print(vid) 
        
        if music==True: # only audio stream is considered
            audio_streams=vid.audiostreams
            print(audio_streams)
        
            for audiostream in audio_streams:
                print("audio stream: ")
                extension=audiostream.extension
                print(extension)
                bitrate=audiostream.bitrate
                print(bitrate)
                filesize=audiostream.get_filesize()
                filesize_MB=round((filesize/1024)/1024,2)
                print("Size is "+str(filesize)+" bytes ("+str(filesize_MB)+" MB)")

                if audiostream.extension=='m4a':
                    #download 
                    audiostream.download(path)
                    
        else:
            best_stream=vid.getbest() # get the best video stream and download it 
            filename=best_stream.download(path)
      