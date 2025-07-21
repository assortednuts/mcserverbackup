import schedule
import time
import datetime
import os
import shutil

# Pick your time zone and when backups should run
timezone = "America/Chicago"
backupTime = "03:00"

def backup():
    getDate = datetime.datetime.now().isoformat()
    os.makedirs("/home/"+os.getlogin()+"/minecraft-server/backups/" + getDate)
    shutil.copytree("/home/"+os.getlogin()+"/minecraft-server/world", "/home/"+os.getlogin()+"/minecraft-server/backups/" + getDate + "/world")
    shutil.copytree("/home/"+os.getlogin()+"/minecraft-server/world_nether", "/home/"+os.getlogin()+"/minecraft-server/backups/" + getDate + "/world_nether")
    shutil.copytree("/home/"+os.getlogin()+"/minecraft-server/world_the_end", "/home/"+os.getlogin()+"/minecraft-server/backups/" + getDate + "/world_the_end")

schedule.every().day.at(backupTime, timezone).do(backup)

while True:
    schedule.run_pending()
    time.sleep(60)
