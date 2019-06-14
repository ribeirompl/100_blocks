import os
import time
import random
import subprocess
from datetime import datetime

def play_sound():
    tune_options = []
    for filename in os.listdir("./tunes/"):
        if filename.endswith(".mp3") or filename.endswith(".wav"):
            tune_options.append(filename)
    
    if len(tune_options)==0:
        return
    else:
        tune_filename = "./tunes/" + random.choice(tune_options)
    subprocess.call(["ffplay", "-loglevel", "panic", "-nodisp", "-autoexit", tune_filename])


def update_screen(num_blocks=0, wake_up_timestamp=7):
    clear_screen()
    print()
    for i in range(10):
        print("    ",end='')
        for j in range(10):
            if i*10+j+1<=num_blocks:
                print(u"\u25A0 ",end='')
            else:
                print(u"\u25A1 ",end='')
        if i<9:
            print()
    print(" " + str(num_blocks) + "/100\n")
    sleep_timestamp = wake_up_timestamp+16
    if sleep_timestamp >=24:
        sleep_timestamp -=24
    print("Wake up: " + str(wake_up_timestamp) + "h00    Bedtime: " + str(sleep_timestamp).zfill(2) + "h40\n")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def cur_blocks(timestamp):
    cur_hour = datetime.now().time().hour
    cur_minute = datetime.now().time().minute
    cur_num_blocks = (cur_hour-timestamp)*6 + cur_minute//10
    return cur_num_blocks

def print_10_min():
    clear_screen()
    print()
    print("  ########################")
    print("  #      _               #")
    print("  #  /| / \\   __  o __   #")
    print("  #   | \\_/   ||| | | |  #")
    print("  #                      #")
    print("  ########################")


timestamp = 0
while (not (timestamp==5 or timestamp==6 or timestamp==7 or timestamp==8 or timestamp==9)):
    print("What time this morning to start counting blocks from? (5,6,7,8 or 9)")
    timestamp = int(input())

last_update = cur_blocks(timestamp)
update_screen(last_update,timestamp)

while(1):
    cur_minute = datetime.now().time().minute
    cur_second = datetime.now().time().second
    sleep_time = int((10-cur_minute%10)*60 -60 + (60-cur_second) -1)
    if sleep_time <= 0:
        sleep_time = 1
    time.sleep(sleep_time)

    cur_update = cur_blocks(timestamp)
    
    while (last_update == cur_update):
        cur_update = (datetime.now().time().hour-timestamp)*6 + datetime.now().time().minute//10
    
    if last_update != cur_update:
        print_10_min()
        play_sound()
        for i in range(10):
            print_10_min()
            time.sleep(0.3)
            clear_screen()
            time.sleep(0.3)

        update_screen(cur_update,timestamp)
        
        last_update = cur_update
    
    





