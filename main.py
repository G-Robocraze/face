# importing vlc module
from server1 import start_server
import vlc,os,time
import threading


HOST = "172.16.45.101"
PORT = 8000


#Add the emotions here ...
emotions = ["sad","blink","love","wonder","normal","demo1","demo2","demo3","demo4"]
default_emotion = "loading"

video_dir="videos"
video_path=os.path.join(os.getcwd(), video_dir)

current_emotion = ""

#Used for looping the video
play_again = False


# creating vlc media player object
media_player = vlc.MediaPlayer()



class thread(threading.Thread):
    def __init__(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID
 
        # helper function to execute the threads
    def run(self):
        global play_again
        print("Starting")
        while not play_again:
            pass

        play_again = False
        
            
        print(str(self.thread_name) +" "+ str(self.thread_ID))
        signal_from_server(current_emotion)
        self.run()



def onEnd(event):
    print("End reached")
    
    print("emotion:",current_emotion)
    global play_again
    play_again = True




media_player.toggle_fullscreen()

em = media_player.event_manager()
em.event_attach(vlc.EventType.MediaPlayerEndReached, onEnd)







def play_media(file):
    media = vlc.Media(file)
    media_player.set_media(media)
    media_player.play()

def signal_from_server(emotion) :
        global current_emotion    
        current_emotion = emotion
        
        current_video_file=current_emotion+".mp4"
        fileName=video_path + "/" + current_video_file
       
        if not os.path.isfile(fileName):
            fileName = video_path+ "/" + default_emotion + ".mp4"

        print(fileName)
        play_media(fileName)
        
server_thread = thread("loop",10001)

server_thread.start()


signal_from_server(default_emotion)


start_server(emotions=emotions,host=HOST,port=PORT,callback=signal_from_server)

