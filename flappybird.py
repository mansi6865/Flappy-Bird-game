from numpy import maximum
import pygame
import random
pygame.init()
screen= pygame.display.set_mode((700,700))
#This is used to display a window of the desired size.
#The return value is a Surface object which is the object where we will perform graphical operations.

bg_image= pygame.image.load('background.png')
bird_image= pygame.image.load('bird.png')
bird_x= 50
bird_y= 300
bird_y_change= 0

clock = pygame.time.Clock()

def display_bird(x,y):
    screen.blit(bird_image, (x,y))

#obstacles
obs_width= 80
obs_height= random.randint(200,450)
#this height for first iteration 
obs_color= (155,255,0)
obs_x_change= -2
#the obstacles will start moving from right to left
obs_x= 700

def display_obstacle(height):
    pygame.draw.rect(screen, obs_color, pygame.Rect(obs_x, 0, obs_width, height))
    bottom_y = height + 160 
    #160 is the space between my top and bottom pbstacles
    bottom_height = 680 - bottom_y
    pygame.draw.rect(screen, obs_color, pygame.Rect(obs_x, bottom_y, obs_width, bottom_height))

def collision_detection(obs_x, obs_height, bird_y, bottom_y):
    if obs_x >= 50 and obs_x <=(50+50):
        #obstacle has to be at the same x as bird, bird is of 50 pixels
        if bird_y <= obs_height or bird_y >= (bottom_y- 50):
            return True
    return False

score= 0
score_font= pygame.font.SysFont('impact', 28)

def display_score(score):
    display=score_font.render("Score: "+ str(score),True, (255,255,255))
    screen.blit(display, (15,15))

running= True

while running:
    screen.fill((0,0,0))
    screen.blit(bg_image, (0,0))
    clock.tick(200)

    for event in pygame.event.get():
        #for every event in pygame
        if event.type == pygame.QUIT:
            #pressing exit will exit the while loop and pygame quits
            running= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change= -3
                #because the origin is at the top left of the screen so negative means bird goes up when spacebar is pressed
        if event.type == pygame.KEYUP:
            #bird goes down once spacebar is released
            if event.key == pygame.K_SPACE:
                bird_y_change= 1
    
    bird_y += bird_y_change
    
 #adding boundaries
    if bird_y <= 0:
        bird_y = 0
    if bird_y >= 645:
        bird_y= 645

    obs_x += obs_x_change
    if obs_x <= -5:
        obs_x= 700
        #everytime the bird passes one obstacle score will increase by 1
        obs_height= random.randint(250,450)
        score += 1
    display_obstacle(obs_height)
   
    collision= collision_detection(obs_x, obs_height, bird_y, obs_height+160)
    
    if collision:
        pygame.quit()


    display_bird(bird_x, bird_y)
    display_score(score)
    
    pygame.display.update()
    #each time we iterate the while loop, the display updates everytime

pygame.quit()
