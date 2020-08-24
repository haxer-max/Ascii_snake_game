from os import system
from random import randint
import msvcrt,time
import numpy as np

system('cls')
speed=2
speed=1/speed/2
#▓9619
#█9608
#▒ 9618
#░ 9617
l=15
b=15
sl=5
sb=5

alive=True
skip=False
wallc=chr(9608)*2
headc=chr(9618)*2
bodyc=chr(9617)*2
spacec=' '*2
space=0
wall=-1
snake=1
up='w'
left='a'
right='d'
down='s'
direc=up
breaks=False

area=np.zeros((l,b))

for i in range(l):
    for j in range(b):
        if i==0 or i==l-1 or j==0 or j==b-1:
            area[i,j]=-1
        elif i==sl and j==sb:
            area[i,j]=1

input("press Enter to start")
#print(randint(0,10))
system('cls')

while alive==True:
        
    for i in range(l):
        for j in range(b):
                if area[i,j]==1:
                    if skip==True:
                        skip=False
                        continue
                    if direc==up:
                        if area[i-1,j]==0:
                            area[i-1,j]=1
                        else:
                            breaks=True
                    elif direc==left:
                        if area[i,j-1]==0:
                            area[i,j-1]=1
                        else:
                            breaks=True
                    elif direc==right:
                        skip=True
                        if area[i,j+1]==0:
                            area[i,j+1]=1
                        else:
                            breaks=True
                    elif direc==down:
                        skip=True
                        if area[i+1,j]==0:
                            area[i+1,j]=1
                        else:
                            breaks=True
                    area[i,j]=0
    system('cls')                
    print(direc)   #for debugging                     
    for e in area:
        for f in e:
            if f==space:
                print(spacec,end='')
            elif f==wall:
                print(wallc,end='')
            elif f==1:
                print(headc,end='')
            else:
                print('_',end='') #debugging
        print("")
    
    time.sleep(speed)
    
    if msvcrt.kbhit():
        direc=chr(ord(msvcrt.getch()))
        if direc!=up and direc!=right and direc!=left and direc!=down:
            break
    if breaks==True:
        break
    
    















