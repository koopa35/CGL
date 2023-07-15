import pygame
import numpy as np

#USER INPUTS FOR DIFFERNT RENDER
RES = WIDTH, HEIGHT = 1600, 900
FPS = 10
SIZE = 10 #Pixel Size for Alive
DENSITY = 10 #Higher NUMBER is Less Dense

#Pygame setup acording to res
pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
running = True


#Creates a matrix representing the gameboard of ones and zeros
SQUARE_RES = SWIDTH, SHEIGHT = WIDTH//SIZE, HEIGHT//SIZE
GAMEBOARD = np.random.choice([0]*DENSITY + [1], size=(SWIDTH, SHEIGHT))
               
#Counts alive cells nearby
def NEIGHBORS(X, Y, GAMEBOARD):
    NEIGHBOR_COUNT = 0
    #Edge Case Top Left
    if(X == 0 and Y == 0):
        if(GAMEBOARD[X + 1][Y] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X][Y+1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X+1][Y+1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
    #Edge Case Top Right
    elif(X == SWIDTH-1 and Y == 0):
        if(GAMEBOARD[X-1][Y] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X][Y+1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X-1][Y+1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1   
    #Edge Case Bot Left
    elif(X == 0 and Y == SHEIGHT):
        if(GAMEBOARD[X + 1][Y] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X][Y-1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X+1][Y-1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
    #Edge Case Bot Right
    elif(X == SWIDTH and Y == SHEIGHT):
        if(GAMEBOARD[X-1][Y] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X][Y-1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X-1][Y-1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1 
    #Edge Case Top Row
    elif(Y == 0):
        if(GAMEBOARD[X-1][Y] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X+1][Y] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X][Y+1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X-1][Y+1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X+1][Y+1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
    #Edge Case Bot Row
    elif(Y == SHEIGHT):
        if(GAMEBOARD[X-1][Y] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X+1][Y] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X][Y-1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X-1][Y-1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X+1][Y-1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1            
    #Edge Case Left Col
    elif(X == 0):
        if(GAMEBOARD[X][Y-1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X][Y+1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X+1][Y] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X+1][Y+1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X+1][Y-1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
    #Edge Case Right Col
    elif(X == SWIDTH):
        if(GAMEBOARD[X][Y-1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X][Y+1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X-1][Y] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X-1][Y+1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X-1][Y-1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
    #Normal Case
    else:
        if(GAMEBOARD[X+1][Y] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X-1][Y] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X][Y+1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X][Y-1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X+1][Y+1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X+1][Y-1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X-1][Y+1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
        if(GAMEBOARD[X-1][Y-1] == 1):
            NEIGHBOR_COUNT = NEIGHBOR_COUNT + 1
    return(NEIGHBOR_COUNT)


#Polls for new ingame events (our case is the exit button)
#pygame.quit() means the user clicked the X in the window
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Clears last frame and draws gameboard
    screen.fill("black")
    XINDEX = 0
    for row in GAMEBOARD:
        YINDEX = 0
        for col in row:
            if GAMEBOARD[XINDEX][YINDEX] == 1:
                pygame.draw.rect(screen, "white", [XINDEX * SIZE, YINDEX * SIZE, SIZE, SIZE])
            YINDEX = YINDEX + 1
        XINDEX = XINDEX + 1

    
    #Uses NEIGHBORS Function to Determine What Happens with Each Population 
    # According to Conways Game of Life when W is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        for X in range(SWIDTH - 1):
            for Y in range(SHEIGHT - 1):
                COUNT = NEIGHBORS(X, Y, GAMEBOARD)
                if (COUNT < 2):
                    GAMEBOARD[X][Y] = 0
                elif (COUNT > 3):
                    GAMEBOARD[X][Y] = 0
                elif (COUNT == 3):
                    GAMEBOARD[X][Y] = 1

    #Displays the game with flip()
    pygame.display.flip()

    #FrameRate
    clock.tick(FPS)

pygame.quit()


