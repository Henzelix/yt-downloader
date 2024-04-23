from pytube import YouTube
from pprint import pprint

def download_4k_video(url, res):
    # Initialize a YouTube object with the URL
    yt = YouTube(url)
    
    # Filter the streams to only include video (no audio) and get the highest resolution ("2160p" is 4K)
    pprint(yt.streams)
    video_stream = yt.streams.filter(res=res, only_video=True).first()
    
    # Check if a 4K video stream is available
    if video_stream:
        # Download the video
        print("\n\nDownloading...\n\n")
        video_stream.download('./download')
        print("Download completed!")
    else:
        print("Video or resolution not available")

# Example URL of a YouTube video
youtube_url = str(input("Insert URL: "))
quality = str(input("Insert quality (e.g. 2160p): "))

# Call the function with the YouTube video URL
download_4k_video(youtube_url, quality)