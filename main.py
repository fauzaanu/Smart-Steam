# a steam control script to change the download speed of steam settings download speed when the internet is slow

import os
import time
import sys

# open the steam config file and change the speed
def change_speed(speed:int):
    speed = str(speed)
    with open("C:\\Program Files (x86)\\Steam\\config\\config.vdf", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if "DownloadThrottleKbps" in lines[i]:
                lines[i] = "\t\t\"DownloadThrottleKbps\"\t\t\"" + speed + "\"\r"

    with open("C:\\Program Files (x86)\\Steam\\config\\config.vdf", "w") as f:
        f.writelines(lines)

    # print the throttle speed line from config file 
    with open("C:\\Program Files (x86)\\Steam\\config\\config.vdf", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if "DownloadThrottleKbps" in lines[i]:
                print(lines[i])


# check if steam is running and exit the program before setting the speed
def check_steam():
    if "steam.exe" in os.popen("tasklist").read():
        print("Steam is running")
        #exit steam
        os.system("taskkill /f /im Steam.exe")
        time.sleep(5)
        return True
    else:
        print("Steam is not running")
        return False




# run the main function
if __name__ == "__main__":

    # if statement just forces steam to be closed before changing the speed
    if check_steam():
        change_speed(1)
        # re-open steam
        os.system("start steam://open/main")
    else:
        change_speed(1)




