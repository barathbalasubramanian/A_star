import pygame
import time
import random
import copy
import math

pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption('GAME OF LIFE')


EMPTY_DICT = {}
make = True
clicked = 0
red = False
green = False
redpos = []
greenpos =[]
neigh_pnt = []
neighbour_points = {}
dis = {}
selected = []
current_red_point_ = []
min_ = []
run = True
upstacles = []
redbox = []

def pic() :
    global EMPTY_DICT
    for i in range(10) :
        for j in range(10) :
            EMPTY_DICT[(i,j)] = 0
            
def drawred() :
    pygame.draw.rect(screen,(255,0,0),pygame.Rect((redpos[0][0]//50)*50,(redpos[0][1]//50)*50,50,50))
    
def drawgreen() :
    pygame.draw.rect(screen,(0,0,0),pygame.Rect((greenpos[0][0]//50)*50,(greenpos[0][1]//50)*50,50,50))

    
def distance(x1,y1,x2,y2) :
    
    d1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    dis[d1] = (x1,y1)

def min_distance() :
    global run
    global current_red_point_
    for i in dis.keys() :
        min_.append(i)
    min_dis = min(min_)
    
    if min_dis == 0 :
        time.sleep(2)
        run = False
        
    else :
        selected_tile = dis[min_dis]
        selected.append(selected_tile)
        for current_red_point in selected :
            X1,Y1 = current_red_point[0]+1 , current_red_point[1]
            X2,Y2 = current_red_point[0] , current_red_point[1]+1
            X3,Y3 = current_red_point[0]-1 , current_red_point[1]
            X4,Y4 = current_red_point[0] , current_red_point[1]-1
            X5,Y5 = current_red_point[0]+1 , current_red_point[1]+1
            X6,Y6 = current_red_point[0]-1 , current_red_point[1]-1
            X7,Y7 = current_red_point[0]+1 , current_red_point[1]-1
            X8,Y8 = current_red_point[0]-1 , current_red_point[1]+1 
            POINTS = [(X1,Y1),(X2,Y2),(X3,Y3),(X4,Y4),(X5,Y5),(X6,Y6),(X7,Y7),(X8,Y8)]
            for i in POINTS :
                try :
                    if EMPTY_DICT[i] != 2 :
                        current_red_point_.append(i)
                except KeyError :
                    pass
            neigh_pnt.append(current_red_point_)
            current_red_point_ = []

while run :
    screen.fill((0,150,150))
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                for i in range(10) :
                    rand_x = random.randint(0,9)
                    rand_y = random.randint(0,9)
                    upstacles.append((rand_x,rand_y))

        if clicked < 2 :
            if event.type == pygame.MOUSEBUTTONDOWN :
                pos = pygame.mouse.get_pos()
                if clicked == 0 :
                    clicked = 1
                    redpos.append(pos)
                    if EMPTY_DICT[(redpos[0][0]//50),(redpos[0][1]//50)] == 0 :
                        EMPTY_DICT[(redpos[0][0]//50),(redpos[0][1]//50)] = 1
                        red = True

                else :
                    greenpos.append(pos)
                    if EMPTY_DICT[(greenpos[0][0]//50,greenpos[0][1]//50)] == 0 :
                        EMPTY_DICT[(greenpos[0][0]//50),(greenpos[0][1]//50)] = 1
                        green = True
                        clicked = 2
                    else :
                        greenpos = []
                        
    for i in upstacles :
        pygame.draw.rect(screen,(255,255,255),pygame.Rect(i[0]*50+10,i[1]*50+10,20,20))
        EMPTY_DICT[i] = 2    
    
    if len(neigh_pnt) > 0 :
        # print(len(neigh_pnt[len(neigh_pnt)-1]))
        for i in neigh_pnt[len(neigh_pnt)-1] :
            distance(i[0],i[1],greenpos[0][0]//50,greenpos[0][1]//50)

        min_distance()
                        
    if len(selected) > 0 :
        for i in selected :
            pygame.draw.rect(screen,(0,255,0),pygame.Rect(i[0]*50,i[1]*50,50,50))   

    for keys in EMPTY_DICT.keys() :
        pygame.draw.rect(screen , (255,255,255) ,pygame.Rect(keys[0]*50,keys[1]*50,50,50),1)
            
    if red :
        drawred()
        if green == True :
            if len(neigh_pnt) < 1 :
                for points in redpos :
                    x , y = points[0]//50 , points[1]//50
                    X1,Y1 = x+1 , y
                    X2,Y2 = x , y+1
                    X3,Y3 = x-1 , y
                    X4,Y4 = x , y-1
                    X5,Y5 = x+1 , y+1
                    X6,Y6 = x-1 , y-1
                    X7,Y7 = x+1 , y-1
                    X8,Y8 = x-1 , y+1   
                    POINTS = [(X1,Y1),(X2,Y2),(X3,Y3),(X4,Y4),(X5,Y5),(X6,Y6),(X7,Y7),(X8,Y8)]
                    for i in POINTS :
                        try :
                            if EMPTY_DICT[i] != 2 :
                                redbox.append(i)
                        except KeyError :
                            pass
                    neigh_pnt.append(redbox)
                    redbox = []

    if green :
        drawgreen()
        
    if  make == True :   
        pic()
        make = False
            
    pygame.display.flip()
