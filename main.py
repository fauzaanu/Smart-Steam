# a steam control script to change the download speed of steam settings download speed when the internet is slow

import os
import time
import sys


THROTTLE_SPEED = 100
FULL_SPEED = 600


# open the steam config file and change the speed
def change_speed(speed:int):
    speed = convert_to_kbps(speed)
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
def steam_is_running():
    """
    check if steam is running
    """
    if "steam.exe" in os.popen("tasklist").read():
        print("Steam is running")
        # #exit steam
        # os.system("taskkill /f /im Steam.exe")
        # time.sleep(5)
        return True
    else:
        print("Steam is not running")
        return False


def kill_steam():
    """
    kill steam
    """
    os.system("taskkill /f /im Steam.exe")
    time.sleep(5)

def convert_to_kbps(speed):
    """
    convert KBPS speed to kilobits per second
    """
    # THROTTLE_SPEED and FULL_SPEED are in kbps while steam config uses kilobits 
    # we should convert the speed to kilobits
    return speed * 8
    




# run the main function
if __name__ == "__main__":
    # if statement just forces steam to be closed before changing the speed
    if steam_is_running():
        kill_steam()
        change_speed(THROTTLE_SPEED)
        # re-open steam
        os.system("start steam://open/main")
    else:
        change_speed(1)




