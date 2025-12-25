import pygame
from sys import exit
# pygame setup
pygame.init()

#game vars
GAME_W = 1100
GAME_H = 700

screen = pygame.display.set_mode((GAME_W, GAME_H))
clock = pygame.time.Clock()
pygame.display.set_caption("Cat Game")
create_logs_timer = pygame.USEREVENT + 0
pygame.time.set_timer(create_logs_timer, 1500) #every 1.5 secs
#log class
log_y = GAME_H
log_x = 0
log_width = 733
log_height = 180

class Log(pygame.Rect):
    def  __init__ (self, img):
        pygame.Rect.__init__(self, log_x, log_y, log_width, log_height)
        self.img = img
        self.passed = False
#cat class
cat_x = GAME_W/2.5
cat_y = GAME_H/2

class Cat(pygame.Rect):
    def  __init__ (self, img):
        pygame.Rect.__init__(self, cat_x, cat_y, 200, 200)
        self.img = img




#game imgs
background_img = pygame.image.load('assets\grass.png')
player = pygame.image.load('assets\cat-back.png')
left_log_img = pygame.image.load('assets\left-log.png')
right_log_img = pygame.image.load('assets\cight-log.png')


#game logic
cat = Cat(player)
logs = []


def draw():
    screen.blit(background_img,(0,0))
    screen.blit(cat.img, cat)

    for log in logs:
        screen.blit(log.img , log)

def create_logs():
    left_log = Log(left_log_img)
    logs.append(left_log)
    #right_log = Log(right_log_img)
    #logs.append(right_log)

    print(len(logs))



player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


while True: #game loop
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    '''
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True: #left
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True: #right
        player.move_ip(1,0)
    elif key[pygame.K_w] == True: #up
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True: #down
        player.move_ip(0,1)
    '''
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == create_logs_timer:
            create_logs()


    draw()
    pygame.display.update()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()