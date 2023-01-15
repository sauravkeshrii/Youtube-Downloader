# importing the module (Pytube may show errors, it depends on Python version)
from pytube import YouTube
from pytube import Search


# download location of the file :
DOWNLOAD_PATH = "C:/Users/saura/Downloads/"

# link of the video to be downloaded :
link = "https://youtu.be/oQdxL_WW3aE"

try:
    # creating youtube object using YouTube
    youtube_obj = YouTube(link)
except:
    print("Connection Error") #to handle exception
    
# filters out all the files with "mp4" extension
mp4files = youtube_obj.streams.filter('mp4')

# to set the name of the files
youtube_obj.set_filename('Downloaded Video')

# get the video with the extension and
# resolution passed in the get() function  
d_video = youtube_obj.get(mp4files[-1].extensions, mp4files[-1].resolution)

try:
    #downloading the video
    d_video.download(DOWNLOAD_PATH)
except:
    print("This is Some Error!")
    
print("Task is completed!")

# fetch Video title
yt = YouTube('https://youtu.be/oQdxL_WW3aE')
print(yt.title)

# get the thumbnail title :
print(yt.thumbnail_url)

# Advance Way to Create YouTube Object :
yt = YouTube(
    'https://youtu.be/oQdxL_WW3aE',
    on_progress_callback=progress_func,
    on_complete_callback=complete_func,
    proxies=my_proxies,
    use_oauth=False,
    allow_oauth_cache=True,
    )

# on_process_callback - This function is used for downloading data chunks from a video.
# on_complete_callback - This function will execute when the video is fully downloaded.
# use_oauth and allow_oauth_cache - This allows us to authorize pytube to interact with the YouTube user account.

# Subtitle/ Caption Tracks ::
yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
yt.captions

# english caption
caption = yt.captions.get_by_language_code('en')  

# caption format
caption.xml_captions

# Python Search Features
s = Search('Cricket World Cup')
s.results

# Searches also have autocomplete suggestions.
s.completion_suggestions
