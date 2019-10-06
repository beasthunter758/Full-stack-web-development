#The below program does not work for linux based distros.
import time
import webbrowser

total_breaks=6

break_count=0


print("This program started on"+time.ctime())

while(break_count<total_breaks):
    time.sleep(2*60*60)
webbrowser.open('https://www.youtube.com/watch?v=sUz6yLJ3e7o',new=0)
break_count=break_count + 1

