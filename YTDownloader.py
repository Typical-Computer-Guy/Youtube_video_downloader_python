from pytube import YouTube # import required modules

save_path = "E:/" # where to save the video file

link="https://www.youtube.com/watch?v=A3RXxmyuhF4"  # link of the video to be downloaded , replace it with the link of the video you need to download
#NOTE: the given link downloads a video on how to encrypt files on windows for free offline with command prompt only

# the computer running this python file may not have internet connection so this raises an error
try:
	yt = YouTube(link) # get the video
except:
	print("Error!") #if you have a problem in getting the link , that is, the link is invalid

required_video=yt.streams.get_highest_resolution() # select the highest resolution of the video

# try saving the video in the path given
try:
	print("download started") # print message that the download
	required_video.download(save_path)
except:
	print("Error!") # could not save file , error
print('downloaded') # video downloaded successfully

