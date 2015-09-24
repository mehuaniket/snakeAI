#!/usr/bin/env python

# Raspberry Snake
# Written by Gareth Halfacree for the Raspberry Pi User Guide
# rewritten by Aniket patel 
# make snake that eat raspberry itself :)

import pygame, sys, time, random
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()

playSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('SnakeAI')
outberry=0
outberrydir='right'
redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)
snakePosition = [100,100]
snakeSegments = [[100,100],[80,100],[60,100]]
raspberryPosition = [300,300]
raspberrySpawned = 1
direction = 'right'
#changeDirection is for what will next direction snake and to take 
changeDirection = direction
#global flag is use when raspberry is in wrong side and snake have to turn to go in specific location
global flag
flag=True
#dirout variable is uses when raspberry position is in wrong side and snake must turn 
#to go in checkdir output location and ignoring direction results  whatinput() function
dirout='right'

#when snake crash function called
def gameOver():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
    gameOverSurf = gameOverFont.render('Game Over', True, greyColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()
#function called when raspberry position out of accessible location by whatinput() function 
def checkdir():
    global flag
    global dirout
    if changeDirection == 'right':
        if snakePosition[0] > raspberryPosition[0]:
            print ("in checkdir if right")
            flag=False
            dirout='down'
            print("log in checkdir :"+dirout)
            
    if changeDirection == 'left':
        if snakePosition[0] < raspberryPosition[0]:
            print ("in checkdir if left")
            flag=False
            dirout='up'
            print("log in checkdir :"+dirout)
     
    if changeDirection == 'up':
        if snakePosition[1] < raspberryPosition[1]:
            print ("in cheakdir if up")
            flag=False
            dirout='right'
            print("log in checkdir :"+dirout)
            
    if changeDirection == 'down':
        if snakePosition[1] > raspberryPosition[1]:
            print ("in cheackdir if down")
            flag=False
            dirout='left'
            print("log in checkdir :"+dirout)
            
#function always called when snake is in direction where raspberry position can be match        
#this function is take status of current direction and make  decision next direction            
def  whatinput():

    if direction == 'right':
        if snakePosition[0] == raspberryPosition[0]:
            if snakePosition[1] < raspberryPosition[1]:
                return 'down'
            else:
                return 'up'
        else:
            return 'right'
    if direction == 'left':
        if snakePosition[0] == raspberryPosition[0]:
            if snakePosition[1] < raspberryPosition[1]:
                return 'down'
            else:
                return 'up'
        else:
            return 'left'
    if direction == 'up':
        if snakePosition[1] == raspberryPosition[1]:
            if snakePosition[0] < raspberryPosition[0]:
                return 'right'
            else:
                return 'left'
        else:
            return 'up'
    if direction == 'down':
        if snakePosition[1] == raspberryPosition[1]:
            if snakePosition[0] < raspberryPosition[0]:
                return 'right'
            else:
                return 'left'
        else:
            return 'down'
    
while True:
  
    #i don't remove the event block that can use to operate snake with keys because some might intrested
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
 
            if event.key == K_RIGHT or event.key == ord('d'):
                changeDirection = 'right'
            if event.key == K_LEFT or event.key == ord('a'):
                changeDirection = 'left'
            if event.key == K_UP or event.key == ord('w'):
                changeDirection = 'up'
            if event.key == K_DOWN or event.key == ord('s'):
                changeDirection = 'down'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))



## this block is give direction movement if snake going to crash with wall
##    if (snakePosition[0]<=40 or snakePosition[1]<=620):
##        if(direction=='left'):
##            changeDirection='down'
##        else:
##            changeDirection='right' 
##    elif (snakePosition[0]<=620 or snakePosition[1]<=40):
##        if(direction=='right'):
##            changeDirection='down'
##        else:
##            changeDirection='left'
##    elif (snakePosition[0]<=620 or snakePosition[1]<=460):
##        if(direction=='down'):
##            changeDirection='left'
##        else:
##            changeDirection='up'
##    elif (snakePosition[0]<=40 or snakePosition[1]<=460):
##        if(direction=='left'):
##            changeDirection='up'
##        else:
##            changeDirection='right'
##    else:

#flag initially true for checking snake will have raspberry position accessible or not
    flag=True
#this might print the stat of the directon that really help you out to code other thinks that snake never crash :)     
    print("current direction :"+changeDirection)

#call checkdir() function to check raspberry position is accessible or not
    checkdir()
    changeDirection=dirout
    print("log checkdir after :"+dirout)
#if flag still true than call second function to do regular things
    if(flag==True): 
        changeDirection = whatinput()
        print("log if flage TRUE :"+dirout)

# following few lines checking that input is reverse direction to current input than block can not take input
#issue:if out whatinput() function  continue input of same direction than might snake will crash:( 
    if changeDirection == 'right' and not direction == 'left':
        direction = changeDirection
    if changeDirection == 'left' and not direction == 'right':
        direction = changeDirection
    if changeDirection == 'up' and not direction == 'down':
        direction = changeDirection
    if changeDirection == 'down' and not direction == 'up':
        direction = changeDirection
    if direction == 'right':
        snakePosition[0] += 20
    if direction == 'left':
        snakePosition[0] -= 20
    if direction == 'up':
        snakePosition[1] -= 20
    if direction == 'down':
        snakePosition[1] += 20

    snakeSegments.insert(0,list(snakePosition))
    if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
        raspberrySpawned = 0
    else:
        snakeSegments.pop()
#if raspberry is spawned that generate next raspberry location with random function
    if raspberrySpawned == 0:
        x = random.randrange(1,32)
        y = random.randrange(1,24)
        raspberryPosition = [int(x*20),int(y*20)]
    raspberrySpawned = 1
    playSurface.fill(blackColour)
    for position in snakeSegments:
        pygame.draw.rect(playSurface,whiteColour,Rect(position[0], position[1], 20, 20))
    pygame.draw.rect(playSurface,redColour,Rect(raspberryPosition[0], raspberryPosition[1], 20, 20))
    pygame.display.flip()
#following code will make gameover when it crash with wall
    if snakePosition[0] > 620 or snakePosition[0] < 0:
        gameOver()
    if snakePosition[1] > 460 or snakePosition[1] < 0:
        gameOver()
    for snakeBody in snakeSegments[1:]:
        if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
            gameOver()
    fpsClock.tick(9)
    print("\n")
