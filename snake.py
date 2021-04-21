from os import system
from random import randint
import msvcrt,time
import numpy as np

system('cls')
speed=5
speed=1/speed/2
#▓9619
#█9608
#▒ 9618
#░ 9617
l=15
b=15
sl=6
sb=6

alive=True
skip=False
wallc=chr(9608)*2
headc=chr(9618)*2
bodyc=chr(9617)*2
foodc=chr(9619)*2
spacec=' '*2
space=0
wall=-1
snake=5
up='w'
left='a'
right='d'
down='s'
direc=up
breaks=False
eaten=False
score=0

foodie=randint(1, (l-2)*(b-2)-snake)

area=np.zeros((l,b))

for i in range(l):
    for j in range(b):
        if i==0 or i==l-1 or j==0 or j==b-1:
            area[i,j]=-1
        elif i==sl and j==sb:
            area[i,j]=5
            area[i,j-1]=4
            area[i,j-2]=3
            area[i,j-3]=2
            area[i,j-4]=1
if True:
    cnt=0
    brakie=False
    for i in range(l):
        for j in range(b):
            if area[i,j]==0:
                cnt+=1
                if cnt==foodie:
                    area[i,j]=snake+2
                    brakie=True
                    break
        if brakie==True:
            break

input("press Enter to start")
#print(randint(0,10))
system('cls')

while alive==True:
    if direc==up:
        if area[sl-1,sb]==0 or area[sl-1,sb]==1:
            area[sl-1,sb]=snake+1
        elif area[sl-1,sb]==snake+2:
            eaten=True
            area[sl-1,sb]=snake+1
        else:
            breaks=True
        sl-=1
    elif direc==left:
        if area[sl,sb-1]==0 or area[sl+1,sb]==1:
            area[sl,sb-1]=snake+1
        elif area[sl,sb-1]==snake+2:
            eaten=True
            area[sl,sb-1]=snake+1
        else:
            breaks=True
        sb-=1
    elif direc==right:
        if area[sl,sb+1]==0 or area[sl,sb+1]==1:
            area[sl,sb+1]=snake+1
        elif area[sl,sb+1]==snake+2:
            eaten=True
            area[sl,sb+1]=snake+1
        else:
            breaks=True
        sb+=1
    elif direc==down:
        if area[sl+1,sb]==0 or area[sl+1,sb]==1:
            area[sl+1,sb]=snake+1
        elif area[sl+1,sb]==snake+2:
            eaten=True
            area[sl+1,sb]=snake+1
        else:
            breaks=True
        sl+=1
    
    if not eaten:
        for i in range(l):
            for j in range(b):
                if area[i,j]>0 and area[i,j]<=snake+1:
                    area[i,j]-=1
    else:
        score+=1
        snake+=1
        foodie=randint(1, (l-2)*(b-2)-snake-1)
        eaten=False
        cnt=0
        brakie=False
        for i in range(l):
            for j in range(b):
                if area[i,j]==0:
                    cnt+=1
                    if cnt==foodie:
                        area[i,j]=snake+2
                        brakie=True
                        break
            if brakie==True:
                break
                    
            
                    

    system('cls')    
    print(foodie)
    print("Score",score)            
    #print(direc)   #for debugging      
    #print(area)  
    #print("hey")             
    for e in area:
        for f in e:
            if f==space:
                print(spacec,end='')
            elif f==wall:
                print(wallc,end='')
            elif f==snake:
                print(headc,end='')
            elif f==snake+2:
                print(foodc,end='')
            elif f>0 :
                print(bodyc,end='')
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
    
    















