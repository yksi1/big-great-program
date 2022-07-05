import random 
import time
import webbrowser

while True: 
    sites = random.choice(["i.imgur.com/yed5Zfk.gif"])
    visit = "https://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randint(1,1.1)
    time.sleep(seconds)
