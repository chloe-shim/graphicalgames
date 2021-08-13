import pygame, random, time

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(r'/Users/prefacecode/PycharmProjects/firstProject/spaceship (1).png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load(r"/Users/prefacecode/PycharmProjects/firstProject/spaceship (1).png")
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = pygame.image.load(r"/Users/prefacecode/PycharmProjects/firstProject/alien (1).png")
enemyX = 450
enemyY = 100
enemyX_change = 7
enemyY_change = 50

#ready - ready to shoot again
#fire - bullet is on the go
bulletImg = pygame.image.load("/Users/prefacecode/PycharmProjects/firstProject/bullet (1).png")
bulletX = 0
bulletY = 480
bulletY_change = 5
bullet_state = "ready"

score = 0
font = pygame.font.Font("freesansbold.ttf", 30)
textX = 10
textY = 10

def show_score(x, y):
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))

def draw_player(x, y):
    screen.blit(playerImg, (x, y))

def draw_enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    if bulletX >= enemyX - 32:
        if bulletX <= enemyX + 32:
            if bulletY <= enemyY + 32:
                return True
    else:
        return False

def collision2(enemyX, enemyY, playerX, playerY):
    if enemyY==480 and ((enemyX == playerX - 50) or (enemyX == playerX + 50)):
        return True
    else:
        return False

def win():
    print("\nCongrats!\n You have successfully completed your mission.")
    print("Here is your trophy reward!")
    trophy = open(r"/Users/prefacecode/PycharmProjects/firstProject/trophy.txt", "r")
    print(trophy.read())
    trophy.close()
    exit()

def game_over():
    gameover_font = pygame.font.SysFont("arial",50) # Choose the font
    gameover_surface = gameover_font.render(f"Game Over! Your final score: {score}",True, (255, 0, 0)) # Creates a surface for our game_over message
    gameover_rect = gameover_surface.get_rect() # Creates a rectangular object for our message
    gameover_rect.midtop = (800 / 2, 600 / 4) # Displays the message in the middle of our screen
    screen.blit(gameover_surface, gameover_rect) # Displays the message on our screen
    pygame.display.flip() # Method to update our whole display
    time.sleep(5) # Add in time delay of 5 seconds before our game quits automatically
    pygame.quit() # Quits the Pygame modules
    quit() # Quits the screen

while True: #the value of running in iteration 1 has to be True

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX #set bullet's x-ccordinate to player's x coord bc thats where we want to fire the bullet from
                    fire_bullet(bulletX, bulletY)#function to fire bullet

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_RIGHT:
                playerX_change = 0


#stopping player movement after reaching edge of the screen
    playerX = playerX_change + playerX
    if playerX <= 0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768

    #making the enemy bounce off the wall as it hits it
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 7
        enemyY += enemyY_change
    elif enemyX >= 768:
        enemyX_change = -7
        enemyY += enemyY_change

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        #short form for bulletY = bulletY_change - bulletY
        bulletY -= bulletY_change

    collision3 = collision2(enemyX, enemyY, playerX, playerY)
    if collision3 == True:
        game_over()

    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision == True:
                bullet_state = "ready"
                bulletY = 400
                score += 1
                enemyX = random.randint(20, 760)
                enemyY = random.randint(50, 150)



    if score == 25:
        win()

    draw_player(playerX, playerY)
    draw_enemy(enemyX, enemyY)
    show_score(textX, textY)
    pygame.display.update()