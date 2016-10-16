# coding: utf-8
# комментарий
import sys
import math
import datetime
import os
import psutil
import shutil

def Info_sys():
    print('Вот, что я знаю о системе:')
    print("Operating System: ", sys.platform)
    print("Count of processes: ", psutil.cpu_count())
    print("Текущая директория: ",os.getcwd())
    print ('Текущий пользователь: ',os.getlogin())
    return "                          ФОРМАТИРУЕМ ДИСК С!"

def main():
    print("I'm Python, HI!")
    name = input("?? Your name: ")
    print(name,", you wanna work? (Y/N)")
    answer = input()

    if answer == "Y" or answer =="y" or answer =="yes" or answer =="YES" or answer =="ye":
        print("Good! Take a gift!")
        print ("[1] - Close the application!")
        print ("[2] - information about your system!")
        print ("[3] - files in this directory!")
        print ("[4] - duplicate files in this directory!")
        print ("[5] - !")
        do = int(input())
        if do == 1:
            print("Close the application!")
            sys.exit()
        elif do == 2:
            Info_sys()
        elif do == 3:
            print("3 maybe: ", math.log10(1000))
            print(os.listdir())
        elif do == 4:
            print("Дублирование файлов в текущей директории: ")
            file_list = os.listdir()
            i = 0
            while i<len(file_list):
                newfile = file_list[i]+".dubl"
                shutil.cope(file_list[i],newfile)
                i=i+1
        else:
            print("I do not understand what you want!")
    elif answer == "N" or answer == "No":
        print("Die! fucker!")
    elif answer == "n" or answer == "no":
        print("Die! fucker!")
    else:
        print ("Stupid men, buy-buy!!!")

if __name__=="__main__":
    main()