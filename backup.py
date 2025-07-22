import schedule
import time
import datetime
import os
import shutil

timezone = "America/Chicago"
backupTime = "03:00"

removeOlderBackups = True
keepBackups = 5

def removeOldest():
    list_of_files = os.listdir('/home/'+os.getlogin()+'/minecraft-server/backups/')
    full_path = ['/home/'+os.getlogin()+'/minecraft-server/backups/{0}'.format(x) for x in list_of_files]

    if len(list_of_files) == keepBackups:
        oldest_file = min(full_path, key=os.path.getctime)
        os.remove(oldest_file)

def backup():

    if removeOlderBackups == True:
        removeOldest()

    getDate = datetime.datetime.now().isoformat()
    os.makedirs("/home/"+os.getlogin()+"/minecraft-server/backups/" + getDate)
    shutil.copytree("/home/"+os.getlogin()+"/minecraft-server/world", "/home/"+os.getlogin()+"/minecraft-server/backups/" + getDate + "/world")
    shutil.copytree("/home/"+os.getlogin()+"/minecraft-server/world_nether", "/home/"+os.getlogin()+"/minecraft-server/backups/" + getDate + "/world_nether")
    shutil.copytree("/home/"+os.getlogin()+"/minecraft-server/world_the_end", "/home/"+os.getlogin()+"/minecraft-server/backups/" + getDate + "/world_the_end")
    shutil.make_archive("/home/"+os.getlogin()+"/minecraft-server/backups/" + getDate, 'zip', "/home/"+os.getlogin()+"/minecraft-server/backups/" + getDate)
    shutil.rmtree("/home/"+os.getlogin()+"/minecraft-server/backups/" + getDate)

schedule.every().day.at(backupTime, timezone).do(backup)

while True:
    schedule.run_pending()
    time.sleep(60)
