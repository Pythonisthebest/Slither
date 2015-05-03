import pygame
from time import sleep
import random

pygame.init()

#---------- Constants ----------#
titleText = 'Slither'
display_width = 800
display_height = 600

font = pygame.font.SysFont(None, 25)

clock = pygame.time.Clock()
FPS = 10

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(titleText)

def snake(x, y,block_size=10):
    """ Draw the snake.

    :param x: X coordinate of snake
    :param y: Y coordinate of snake
    :param block_size: size of the snake
    """
    pygame.draw.rect(gameDisplay, green, [x, y,block_size,block_size])    # snake

def msg_to_screen(msg, color, sleepTime=2):
    """
    :param msg: The message you want to display.
    :param color: The color you want the message to display in.
    :param sleepTime: How long you want the msg to display.
    """
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, (display_width/2, display_height/2))
    pygame.display.update()
    sleep(sleepTime)


def gameLoop():
    #---------- Positions and Block Size ----------#
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    block_size = 10

    #---------- Apple Generation ----------#
    randAppleX = random.randrange(0, display_width-block_size)
    randAppleX = round(randAppleX/10)*10
    randAppleY = random.randrange(0, display_height-block_size)
    randAppleY = round(randAppleY/10)*10

    gameOver = False
    gameExit = False
    while not gameExit:
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameExit = True
            gameOver = True
            msg_to_screen("Out of bounds", red)
        elif gameOver:
            break

        for event in pygame.event.get():
            # print(event)
            ev = event.type
            if ev == pygame.QUIT:
                gameExit = True
            if ev == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # lead_x_change = -(block_size/2)
                    lead_x_change = -block_size
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT:
                    # lead_x_change = (block_size/2)
                    lead_x_change = block_size
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    # lead_y_change = -(block_size/2)
                    lead_y_change = -block_size
                    lead_x_change = 0
                if event.key == pygame.K_DOWN:
                    # lead_y_change = (block_size/2)
                    lead_y_change = block_size
                    lead_x_change = 0
            # if ev == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         lead_x_change = 0
            #     if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #         lead_y_change = 0

        lead_x += lead_x_change     # sum the delta x
        lead_y += lead_y_change     # sum the delta y
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY  ,block_size,block_size])    # apple
        snake(lead_x, lead_y,block_size)
        # pygame.draw.rect(gameDisplay, green, [lead_x, lead_y,block_size,block_size])            # snake
        # pygame.draw.rect(gameDisplay, red, [400,300,10,10])
        # gameDisplay.fill(red, rect=[200,200,50,50])
        pygame.display.update()

        while gameOver:
            gameDisplay.fill(white)
            msg_to_screen("GAME OVER, press c to play again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if ev == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                        break
                    if event.key == pygame.K_c:
                        gameExit = False
                        gameOver = False
                        lead_x = display_width/2
                        lead_y = display_height/2
                        lead_x_change = 0
                        lead_y_change = 0

        if lead_x == randAppleX and lead_y == randAppleY:
            # print('om nom nom')
            randAppleX = random.randrange(0, display_width-block_size)
            randAppleX = round(randAppleX/10)*10
            randAppleY = random.randrange(0, display_height-block_size)
            randAppleY = round(randAppleY/10)*10

        clock.tick(FPS)

    # input()
    pygame.quit()


if __name__=='__main__':
    gameLoop()