import pygame
import random
import time

pygame.init() #Initialises Pygame modules

screen_width = 720
screen_height = 480
pygame.display.set_caption("Snake Game")
screen = pygame.display.set_mode((screen_width,screen_height)) # Creates our game screen
score = 0

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
blue = pygame.Color(0,0,255)
yellow = pygame.Color(255,255,0)
green = pygame.Color(0,255,0)
orange = pygame.Color(255,100,10)
purple = pygame.Color(240,0,255)
pink = pygame.Color(255,100,180)

fps = pygame.time.Clock() #frames per second i.e. refresh your screen corresponding to current game clock

snake_position = [100,50] # Snake starting position
snake_speed = 10
snake_body = [[100,50],[90,50],[80,50],[70,50]] # Start with 4 blocks in our snake
direction = "RIGHT" # Initial direction of travel
change_to = direction

# Fruit position to be randomly placed anywhere on the screen we defined
fruit_position = [random.randrange(1, (screen_width // 10)) * 10, random.randrange(1, (screen_height // 10)) * 10]

fruit_spawn = True

def win():
    print("\nCONGRATULATIONS!\nYou have successfully completed your mission")
    print("Here is your trophy reward!")
    trophy = open("trophy.txt","r")
    print(trophy.read())
    trophy.close()
    exit()

def show_score(color, font, size):
    score_font = pygame.font.SysFont(font,size) # Choose the font
    score_surface = score_font.render(f"Score: {score}", True, color) # Creates a surface for our score to go on
    score_rect = score_surface.get_rect() # Creates a rectangular object for our score
    screen.blit(score_surface,score_rect) # Displays the score on our screen

def game_over():
    gameover_font = pygame.font.SysFont("arial",50) # Choose the font
    gameover_surface = gameover_font.render(f"Game Over! Your final score: {score}",True, red) # Creates a surface for our game_over message
    gameover_rect = gameover_surface.get_rect() # Creates a rectangular object for our message
    gameover_rect.midtop = (screen_width / 2, screen_height / 4) # Displays the message in the middle of our screen
    screen.blit(gameover_surface, gameover_rect) # Displays the message on our screen
    pygame.display.flip() # Method to update our whole display
    time.sleep(5) # Add in time delay of 5 seconds before our game quits automatically
    pygame.quit() # Quits the Pygame modules
    quit() # Quits the screen

while True:
    # To change the direction of our snake
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # To prevent the snake going back on itself
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # To keep the snake moving constantly
    if direction == 'UP':
        snake_position[1] = snake_position[1] - 10
    if direction == 'DOWN':
        snake_position[1] = snake_position[1] + 10
    if direction == 'LEFT':
        snake_position[0] = snake_position[0] - 10
    if direction == 'RIGHT':
        snake_position[0] = snake_position[0] + 10

    # # To grow our snake by 1 block for every fruit it eats
    # snake_body.insert(0, list(snake_position))
    # if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
    #     score = score + 1
    #     speed = speed + 10
    #     fruit_spawn = False
    # else:
    #     snake_body.pop() # removes the last position of the snake body as it moves

    # To grow our snake by 1 block for every fruit it eats
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score = score + 1
        # snake_speed = snake_speed + 10
        fruit_spawn = False
    else:
        snake_body.pop() # removes the last position of the snake body as it moves

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (screen_width // 10)) * 10, random.randrange(1, (screen_height // 10)) * 10]

    fruit_spawn = True
    screen.fill(black) # To refresh the screen with black

    #drawing the blocks of the snake
    for block in snake_body:
        pygame.draw.rect(screen, blue, pygame.Rect(block[0],block[1],10,10))

    #drawing the fruit block
    pygame.draw.rect(screen, white, pygame.Rect(fruit_position[0],fruit_position[1],10,10)) # Draws a new fruit block on screen

    # Game Over Conditions
    # If snake hits a wall
    if snake_position[0] < 0 or snake_position[0] > screen_width:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > screen_height:
        game_over()
    # If snake hits it's own body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    if score == 25:
        win()

    show_score(white,"arial",25)

    pygame.display.update()
    fps.tick(snake_speed)