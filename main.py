import os
import time

second, minute, hour = 0, 0, 0 

while(True):
    print(hour,":",minute,":",second)
    time.sleep(1)
    second += 1
    if(second == 60):
        second = 0
        minute += 1
    if(minute == 60):
        minute = 0
        hour += 1
    os.system('cls')