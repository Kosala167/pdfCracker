import pikepdf
import string
from itertools import product
import os.path
import threading
import time

founded = [False,None]

print("PDF crack 1.0(::KBSOFTLK::)")

print("+++++++++++++++++++++++++++")

print("Ex pass = 'abc' to 'abcd'. start is 3 digits .end is 4 digits")

start = input("Start digit count(Ex: 1)-> ")

end = input("End digit count(Ex: 8)-> ")

try:
    start = int(start)
    end = int(end)
except:
    print("start and end must be integer")
    exit()

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

print("We check only '",chars,"'")

confirm = input("Do you need check custom characters(y,n): ")

if confirm == 'y':
    chars = input("Add your character list: ")

treadCount = input("How many thread do you want to apply at once(Ex: 10) : ")

try:
    treadCount = int(treadCount)
except:
    print("Run on default tread count of 1")
    treadCount = 1

file = input("file name(Ex: example.pdf)-> ")

if os.path.exists(file) != True:
    print("file is not exist")
    exit()

if file.endswith('.pdf') != True:
    print("file is not pdf")
    exit()

def current_milli_time():
    return round(time.time() * 1000)

def checkLastElem(str,check):
    chars = list(str)
    for char in chars:
        if char != check:
            return False
    return True

def craker(pwd,f):
    try:
        # open PDF file
        with pikepdf.open(file, password=pwd) as pdf:
            # Password decrypted successfully, break out of the loop
            f[0] = True
            f[1] = pwd
    except:
        pass
    finally:
        print("password->",pwd," :::Checked")
        

print("+++++++++++++++++++Program begining+++++++++++++++++++")
time.sleep(1)

startAt = current_milli_time()

for length in range(start, end):
    to_attempt = product(chars, repeat=length)
    temp = list()
    for attempt in to_attempt:
        pwd = ''.join(attempt)
        if treadCount > 1:
            temp.append(pwd)
            tempLength = len(temp)
            if tempLength == treadCount or checkLastElem(pwd,chars[-1]):
                treadList = list()
                for tr in temp:
                    treadList.append(threading.Thread(target = craker, args=(tr,founded)))
                for i in treadList:
                    i.start()
                for i in treadList:
                    i.join()
                if founded[0] == True:
                    print("[+][+][+][+][+][+][+][+][+] Password found:", founded[1])
                    break
                if tempLength > 1:
                    print(tempLength," Of passwords checked at once")
                temp = list()
        else:
            craker(pwd,founded)
            if founded[0] == True:
                    print("[+][+][+][+][+][+][+][+][+] Password found:", founded[1])
                    break

print("Total time ",(current_milli_time() - startAt))

last = input("Press Enter for exit ")
