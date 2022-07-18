'''

Video Splitter Utility

	Author	: Viki (@) Vignesh Natarajan 
	Licence	: MIT
	Year    : July, 2022
	Contact : neoviki.com

'''

import sys, os
from moviepy.editor import VideoFileClip
from time import sleep

output_dir='video_out'
filename=None
#in seconds
each_part_duration=None

def usage():
    print("\n    usage: " +str(a0)+" -f <mp4 filename> -d <duration of each part in seconds> -o <output_directory>")
    print("\n    usage: " +str(a0)+" -f <mp4 filename> -c <number of parts to split> -o <output_directory>\n")
    exit(0)

def validate_args():	
    if sys.argv[1] != '-f':
    	print("error: missing filename\n")
    	usage()

    if (sys.argv[3] != '-c') and (sys.argv[3] != '-d'):
    	print("error: missing option -c or -d\n")
    	usage()

    if sys.argv[4]==None:
    	usage()

def parse_arguments():
    global filename, each_part_duration, output_dir

    filename=sys.argv[2]
    option_value=sys.argv[4]	
    #duration in seconds
    video_duration = VideoFileClip(filename).duration

    if (sys.argv[3] == '-c'):
        nparts=int(sys.argv[4])
    else:
        nparts=int(int(video_duration)/int(sys.argv[4]))

    if (sys.argv[6] != None) and (sys.argv[5]=='-o'):
        output_dir=sys.argv[6]

    each_part_duration =int(int(video_duration)/int(nparts))

    print("\nSplitting Video with the following parameters:")
    print("\n")
    print("\n")
    print("             File Name                    : "+filename)
    print("             Input Video Duration (sec)   : "+str(video_duration))
    print("             Duration of each part (sec)  : "+str(each_part_duration))
    print("             Number of parts              : "+str(nparts))
    print("             Output Directory             : "+output_dir)
    print("\n")
    print("\n")

def split_video(filename, each_each_part_duration, output_dir):
    file_index=each_each_part_duration+nparts+2
    video_duration = VideoFileClip(filename).duration

    try:
    	os.mkdir(output_dir)
    except:
    	pass
    try:
        while video_duration > each_each_part_duration:
    	    clip = VideoFileClip(filename).subclip(video_duration-each_part_duration, video_duration)
    	    video_duration -= each_each_part_duration
    	    video_out = str(output_dir)+"/out"+str(file_index)+".mp4"
    	    clip.to_videofile(video_out, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
    	    print("####")
    	    file_index-=1
    except:
        pass

validate_args()
parse_arguments()
split_video(filename, each_part_duration, output_dir)

