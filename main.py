import pygame
import random
xx=0
yy=0
#screen resolution and basic commands
score1=0
score2=0
pygame.display.set_caption('Pong')
pygame.init()
X=1280
Y=720
screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
running = True
dt=0
start=False
#default position of objects
player1_pos = pygame.Vector2(screen.get_width() / 10, screen.get_height() / 2)
player2_pos = pygame.Vector2(screen.get_width() - screen.get_width()/10, screen.get_height() / 2)
ball = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
#ball speed and direction
def ball_random_direction():
    speed=700
    abx = random.uniform(speed/2, speed*3/4)
    aby = (speed**2-abx**2)**(1/2)
    s=random.randint(0, 3)
    if s==0:
        bx=abx
        by=aby
    if s==1:
        bx=-abx
        by=aby
    if s==2:
        bx=abx
        by=-aby
    if s==3:
        bx=-abx
        by=-aby
    return bx,by
b=ball_random_direction()
bx, by = b[0], b[1]
#font
font = pygame.font.Font('slkscr.ttf', 32)
#playerscore
score1, score2 = 0, 0
while running:
    screen.fill((0, 0, 0))
    #closing game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if score1==9 or score2==9:
        if score1 > score2:
            win = font.render("Player 1 won", True, (255, 255, 255))
            winrect = win.get_rect()
            winrect.center = (X // 2, Y // 2)
            screen.blit(win, winrect)
        else:
            win = font.render("Player 2 won", True, (255, 255, 255))
            winrect = win.get_rect()
            winrect.center = (X // 2, Y // 2)
            screen.blit(win, winrect)
        death = True
        running = False

    #drawing score
    scorep1display = font.render(str(score1), True, (255, 255, 255))
    p1rect = scorep1display.get_rect()
    p1rect.center = (X // 4, Y//8)
    screen.blit(scorep1display, p1rect)
    scorep2display = font.render(str(score2), True, (255, 255, 255))
    p2rect = scorep2display.get_rect()
    p2rect.center = (X-X // 4, Y//8)
    screen.blit(scorep2display, p2rect)
    #drawing objects
    pygame.draw.rect(screen, "white", (player1_pos.x, player1_pos.y, 20, 150), 0)
    pygame.draw.rect(screen, "white", (player2_pos.x, player2_pos.y, 20, 150), 0)
    pygame.draw.lines(screen, "white", False, [(screen.get_width() / 2, screen.get_height()), (screen.get_width() / 2, 0)], 2)
    pygame.draw.circle(screen, "white", (ball.x, ball.y), 10, 0)
    dt = clock.tick(60) / 1000
    #controls
    pspeed=500
    keys = pygame.key.get_pressed()
    motion=[False, False,False,False]
    if keys[pygame.K_w]:
        player1_pos.y -= pspeed * dt
        motion[0]=True
    if keys[pygame.K_s]:
        motion[1]=True
        player1_pos.y += pspeed * dt
    if keys[pygame.K_UP]:
        motion[2]=True
        player2_pos.y -= pspeed * dt
    if keys[pygame.K_DOWN]:
        motion[3]=True
        player2_pos.y += pspeed * dt
    if keys[pygame.K_SPACE]:
        start=True
    #ball physics
    if ball.y>=screen.get_height() or ball.y<=0:
        by=-by
    if player1_pos.y <= ball.y <= player1_pos.y+150 and player1_pos.x <= ball.x <= player1_pos.x+20:
        bx=-bx
    if player2_pos.y <= ball.y <= player2_pos.y+150 and player2_pos.x <= ball.x <= player2_pos.x+20:
        bx=-bx
    if start:
        ball.x += bx*dt
        ball.y += by*dt
    if ball.x<=0:
        score2+=1
        ball.x=X//2
        ball.y=Y//2
        b = ball_random_direction()
        bx, by = b[0], b[1]
    if ball.x>=X:
        score1+=1
        ball.x=X//2
        ball.y=Y//2
        b = ball_random_direction()
        bx, by = b[0], b[1]
    print(ball.distance_to((xx, yy)))
    xx=ball.x + bx*dt
    yy=ball.y + by*dt
    pygame.display.flip()
while death:
    clock.tick(1)
    death=False