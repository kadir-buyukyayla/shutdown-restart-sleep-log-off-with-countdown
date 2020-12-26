"""
toplam_saniye= total second
"""


import time
import os

if os.name=="nt":
    os.system("cls")
elif os.name=="posix":
    os.system("clear")
    print("only windows")
    time.sleep(10)
    exit()
else:
    print("only windows")
    time.sleep(10)
    exit()
    
print("========================================================================")
print("choose an option?\n")
secilen=input("Shutdown[1]\t|\tRestart[2]\t|\tLog Out[3]\t|\tSleep[4]\n\n---> ")
try:
    secilen=int(secilen) ############==== chosen value
except:
    print("Value error")
    time.sleep(5)
    exit()
if os.name=="nt":
    os.system("cls")
elif os.name=="posix":
    os.system("clear")
print("========================================================================")
print("enter time value")
saat=input("hour: ") #########=======  hour
dakika=input("minute: ") #########=======  minute
try:
    saat=int(saat)   # try: hour = int(hour)
except:
    print("Value error")
    time.sleep(5)
    exit()
try:
    dakika=int(dakika) # try: minute = int(minute)
except:
    print("Value error")
    time.sleep(5)
    exit()
toplam_saniye=(int(saat)*3600)+(int(dakika)*60) ####=======  total seconds

#--------------------------------------------------------------#
    #if chosen value == 1
    
if secilen==1:
    for i in range(toplam_saniye):
        os.system("cls")
        print("{} seconds left".format(toplam_saniye))
        toplam_saniye-=1
        time.sleep(1)
    os.system("shutdown /s")
    
#--------------------------------------------------------------#
    #elif chosen value == 2
    
elif secilen==2:
    for i in range(toplam_saniye):
        os.system("cls")
        print("{} seconds left".format(toplam_saniye))
        toplam_saniye-=1
        time.sleep(1)
    os.system("shutdown /r")
    
#--------------------------------------------------------------#
    #elif chosen value == 3
elif secilen==3:
    for i in range(toplam_saniye):
        os.system("cls")
        print("{} seconds left".format(toplam_saniye))
        toplam_saniye-=1
        time.sleep(1)
    os.system("shutdown /l")

#--------------------------------------------------------------#
    #elif chosen value == 4

elif secilen==4:
    for i in range(toplam_saniye):
        os.system("cls")
        print("{} seconds left".format(toplam_saniye))
        toplam_saniye-=1
        time.sleep(1)
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0 powercfg -hibernate off")