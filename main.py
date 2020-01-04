import downloader

while True:
    prompt_type=input("Video or playlist? (video/playlist) ")
    
    if prompt_type=='video':
        
        prompt_video_path=input("Enter path to store the video/audio: ")
        prompt_video_url=input("Enter URL or tag: ")
        
        while True:
            
            prompt_audio_only=input("Audio only?(yes/no): ")
        
            if prompt_audio_only=='yes':
                downloader.download_video(prompt_video_url, prompt_video_path, music=True) 
                break
            elif prompt_audio_only=='no':
                downloader.download_video(prompt_video_url, prompt_video_path)
                break
        break

    elif prompt_type=='playlist':
        
        prompt_playlist_path=input("Enter path to store the video playlist/music list: ")
        prompt_playlist_url=input("Enter URL or tag: ")
            
        while True:
            prompt_audio_only=input("Audio only?(yes/no): ")
        
            if prompt_audio_only=='yes':
                downloader.download_playlist(prompt_playlist_url, prompt_playlist_path, music=True) 
                break
            elif prompt_audio_only=='no':
                downloader.download_playlist(prompt_playlist_url, prompt_playlist_path)
                break
        break

               