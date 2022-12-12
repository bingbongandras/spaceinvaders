import pygame
import os
import sys
import random
import math
from pygame.locals import *

pygame.mixer.init()
pygame.font.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1920,1080))
current_time = 0
last_time = 0
as_rotation_time = 0
pygame.display.set_caption('galaxy invaders')
bg = pygame.image.load(os.path.join('data', 'hatter1.png'))

pygame.mouse.set_visible(1)

#Jatekos
ship = pygame.image.load(os.path.join('data', 'Feature2.png'))
ship_top = screen.get_height() - ship.get_height()
ship_left = screen.get_width()/2 - ship.get_width()/2
ship_lives = 3
ship_hit_sound = pygame.mixer.Sound(os.path.join('data', 'alien_killed.wav'))
score = 0
score_text = pygame.font.Font('freesansbold.ttf', 45)

#Lovesek
shots = []
shot_sound = pygame.mixer.Sound(os.path.join('data', 'laser_sound.wav'))

class Shot:
    def __init__(self, x, y):
        self.img = pygame.image.load(os.path.join('data','bulletc.png'))
        self.rect = self.img.get_rect()
        self.x = x
        self.y = y
        self.velocity = 25

#Utkozes
def HasCollided(e_x,e_y,b_x,b_y,required_distance):
    dist = math.sqrt(math.pow(e_x-b_x,2)+math.pow(e_y-b_y,2))
    if dist < required_distance:
        return True
    else:
        return False


#Ellensegek
enemies = []
enemy_death = pygame.mixer.Sound(os.path.join('data','asteroid_explosion.wav'))

class Enemy:
    def __init__(self,x,y):
        self.b_img = pygame.transform.flip(pygame.image.load(os.path.join('data','alien_2.png')),True,True)
        self.img = pygame.transform.scale(self.b_img,(100,100))
        self.rect = self.img.get_rect()
        self.x = x
        self.y = y
        self.velocity = 2

fa_enemies = []

class fast_Enemy:
    def __init__(self,x,y):
        self.b_img = pygame.transform.flip(pygame.image.load(os.path.join('data','alien_1.png')),True,True)
        self.img = pygame.transform.scale(self.b_img,(100,100))
        self.x = x
        self.y = y
        self.x_velocity = 8
        self.velocity = 29

asteroids = []
asteroid_hit_sound = pygame.mixer.Sound(os.path.join('data','big_asteroid_hit.wav'))

class Asteroid:
    def __init__(self,x,y,rot):
        self.img = pygame.transform.rotate(pygame.image.load(os.path.join('data','asteroid.png')),rot)
        self.lives = 1
        self.rotation_time = random.randint(-1,1)
        self.x = x
        self.y = y
        self.x_velocity = random.randint(-5,5)
        self.y_velocity = 2

m_asteroids = []

class mini_Asteroid:
    def __init__(self,x,y,rot):
        self.c_img = pygame.transform.rotate(pygame.image.load(os.path.join('data','asteroid.png')),rot)
        self.img = pygame.transform.scale(self.c_img,(110,110))
        self.rotation_time = random.randint(-1,1)
        self.x = x
        self.y = y
        self.x_velocity = 5
        self.y_velocity = 25

bosses = []

class Boss:
    def __init__(self,x,y):
        self.img = pygame.image.load(os.path.join('data','alien_boss.png'))
        self.lives = 15
        self.rotation_time = random.randint(-1,1)
        self.x = x
        self.y = y
        self.x_velocity = 15
        self.y_velocity = 5

def EnemySpawn():
    if current_time == 25:
        for x in range(3):
            P_enemy = Enemy(random.randint(0,screen.get_width()),-100*x)
            enemies.append(P_enemy)
        for x in range(2):
            P_asteroid = Asteroid(random.randint(0,screen.get_width()),-100*x,random.randint(-180,180))
            asteroids.append(P_asteroid)

    if current_time == 500:
        for x in range(5):
            P_mini_asteroid = mini_Asteroid(random.randint(0,screen.get_width()),-300*x,random.randint(-180,180))
            m_asteroids.append(P_mini_asteroid)
        for x in range(2):
            P_asteroid = Asteroid(random.randint(0,screen.get_width()),-400,random.randint(-180,180))
            asteroids.append(P_asteroid)
    
    if current_time == 750:
        for x in range(32):
            P_mini_asteroid = mini_Asteroid(random.randint(0,screen.get_width()),-300*x,random.randint(-180,180))
            m_asteroids.append(P_mini_asteroid)
    
    if current_time == 1325:
        for x in range(3):
            P_asteroid = Asteroid(random.randint(0,screen.get_width()),-120*x,random.randint(-180,180))
            asteroids.append(P_asteroid)
        for x in range(15):
            P_enemy = fast_Enemy(random.randint(0,screen.get_width()),-400*x)
            fa_enemies.append(P_enemy)
    
    if current_time == 1955:
        for x in range(4):
            P_asteroid = Asteroid(random.randint(0,screen.get_width()),-120*x,random.randint(-180,180))
            asteroids.append(P_asteroid)
        for x in range(12):
            P_enemy = fast_Enemy(random.randint(0,screen.get_width()),-400*x)
            fa_enemies.append(P_enemy)
        for x in range(25):
            P_enemy = Enemy(random.randint(0,screen.get_width()),-100*x)
            enemies.append(P_enemy)
    
    if current_time == 2855:
        for x in range(45):
            P_enemy = Enemy(random.randint(0,screen.get_width()),-100*x)
            enemies.append(P_enemy)
        for x in range(32):
            P_mini_asteroid = mini_Asteroid(random.randint(0,screen.get_width()),-300*x,random.randint(-180,180))
            m_asteroids.append(P_mini_asteroid)
    
    if current_time == 3766:
        for x in range(4):
            P_asteroid = Asteroid(random.randint(0,screen.get_width()),-420*x,random.randint(-180,180))
            asteroids.append(P_asteroid)
        for x in range(3):
            P_asteroid = Asteroid(random.randint(0,screen.get_width()),-120*x,random.randint(-180,180))
            asteroids.append(P_asteroid)

    if current_time == 4200:
          for x in range(1):
            P_boss = Boss(random.randint(0,screen.get_width()),-500)
            bosses.append(P_boss)
        
game_state = 'menu'

while True:
    if game_state == 'menu':
        current_time = 0
        last_time = 0
        asteroids.clear()
        enemies.clear()
        shots.clear()
        m_asteroids.clear()
        fa_enemies.clear()

        pygame.font.init()
        screen.fill((0,0,0))
        screen.blit(bg,(0,0))

        font = pygame.font.Font('freesansbold.ttf', 32)
        title = font.render('Galaxy Invaders',True,(255,255,255),None)
        start = font.render('Nyomdd meg a space-t a kezdéshez!',True,(255,255,255),None)

        screen.blit(title,((screen.get_width()/100)*45,(screen.get_height()/100)*60))
        screen.blit(start,((screen.get_width()/100)*30,(screen.get_height()/100)*20))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    game_state = 'game'
                    print(game_state)

    elif game_state == 'game':
        current_time = current_time + 1
        as_rotation_time = as_rotation_time + .2
        clock.tick(60)

        EnemySpawn()

        screen.fill((0,0,0))
        screen.blit(bg,(0,0))

        x,y = pygame.mouse.get_pos()
        ship_x = x-ship.get_width()/2

        screen.blit(ship, (ship_x, ship_top))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            elif event.type == MOUSEBUTTONDOWN:

                if current_time - last_time >= 22:
                    shot_sound.play()
                    P_Shot = Shot(ship_x,900)
                    shots.append(P_Shot)
                    last_time = current_time

        #lovesek kepernyore rajzolasa
        for shot in shots:
            screen.blit(shot.img,(shot.x,shot.y))
            shot.y = shot.y - shot.velocity

            if shot.y <= 0:
                shots.remove(shot)

            #miket talalt el

            for x in enemies:
                checkColl = HasCollided(x.x,x.y,shot.x,shot.y,45)
                if checkColl == True:
                    if shot in shots:
                        shots.remove(shot)
                        enemies.remove(x)
                        enemy_death.play()
                        score = score + 25
            
            for x in fa_enemies:
                checkColl = HasCollided(x.x,x.y,shot.x,shot.y,45)
                if checkColl == True:
                    if shot in shots:
                        shots.remove(shot)
                        fa_enemies.remove(x)
                        enemy_death.play()
                        score = score + 35

            for x in asteroids:
                checkColl = HasCollided(x.x,x.y,shot.x,shot.y,150)
                if checkColl == True:
                    if shot in shots:
                        shots.remove(shot)
                        if x.lives > 0:
                            x.lives = x.lives-1
                            asteroid_hit_sound.play()
                        else:
                            asteroids.remove(x)
                            enemy_death.play()
                            score = score + 100
            
            for x in m_asteroids:
                checkColl = HasCollided(x.x,x.y,shot.x,shot.y,150)
                if checkColl == True:
                    if shot in shots:
                        shots.remove(shot)
                        m_asteroids.remove(x)
                        enemy_death.play()
                        score = score + 45

            for x in bosses:
                checkColl = HasCollided(x.x,x.y,shot.x,shot.y,150)
                if checkColl == True:
                    if shot in shots:
                        shots.remove(shot)
                        if x.lives > 0:
                            x.lives = x.lives-1
                            asteroid_hit_sound.play()
                        else:
                            bosses.remove(x)
                            enemy_death.play()
                            score = score + 1000
                            game_state = 'game win'

        #kisebb elensegek kepernyore rajzolasa
        for enemy in enemies:
            screen.blit(enemy.img,(enemy.x,enemy.y))
            enemy.y = enemy.y + enemy.velocity

            if enemy.y >= 1080:
                enemies.remove(enemy)

            checkColl = HasCollided(enemy.x,enemy.y,ship_x,ship_top,95)
            if checkColl == True:
                ship_lives = ship_lives-1
                enemies.remove(enemy)
                ship_hit_sound.play()

        for fa_enemy in fa_enemies:
            random_roll = random.randint(1,50)

            if random_roll == 1:
                fa_enemy.x_velocity = -8
            elif random_roll == 50:
                fa_enemy.x_velocity = 8

            if fa_enemy.y >= 1080:
                fa_enemies.remove(fa_enemy)

            screen.blit(fa_enemy.img,(fa_enemy.x,fa_enemy.y))
            fa_enemy.y = fa_enemy.y + fa_enemy.velocity
            fa_enemy.x = fa_enemy.x + fa_enemy.x_velocity

            checkColl = HasCollided(fa_enemy.x,fa_enemy.y,ship_x,ship_top,95)
            if checkColl == True:
                ship_lives = ship_lives-1
                fa_enemies.remove(fa_enemy)
                ship_hit_sound.play()
            
        #nagyobb aszteroida kepernyore rajzolasa
        for asteroid in asteroids:

            if asteroid.x >= 1800:
                asteroid.x_velocity = random.randint(-5,-3)

            if asteroid.x <= 10:
                asteroid.x_velocity = random.randint(3,5)
        
            screen.blit(asteroid.img,(asteroid.x,asteroid.y))
            asteroid.y = asteroid.y + asteroid.y_velocity
            asteroid.x = asteroid.x + asteroid.x_velocity

            if asteroid.y >= 1080:
                asteroids.remove(asteroid)
            
            checkColl = HasCollided(asteroid.x,asteroid.y,ship_x,ship_top,250)
            if checkColl == True:
                ship_lives = ship_lives-1
                asteroids.remove(asteroid)
                ship_hit_sound.play()
        #mini aszteroid kepernyore rajzolasa
        for m_asteroid in m_asteroids:

            if m_asteroid.x >= 1800:
                m_asteroid.x_velocity = random.randint(-5,-3)

            if m_asteroid.x <= 10:
                m_asteroid.x_velocity = random.randint(3,5)
            
            if m_asteroid.y >= 1080:
                m_asteroids.remove(m_asteroid)

            screen.blit(m_asteroid.img,(m_asteroid.x,m_asteroid.y))
            m_asteroid.y = m_asteroid.y + m_asteroid.y_velocity
            m_asteroid.x = m_asteroid.x + m_asteroid.x_velocity

            checkColl = HasCollided(m_asteroid.x,m_asteroid.y,ship_x,ship_top,105)
            if checkColl == True:
                ship_lives = ship_lives-1
                m_asteroids.remove(m_asteroid)
                ship_hit_sound.play()

        #boss kepernyo rajzolasa
        for boss in bosses:
            screen.blit(boss.img,(boss.x,boss.y))

            if boss.x >= (screen.get_width()/100)*85:
                boss.x_velocity = -5
            if boss.x <= (screen.get_width()/100)*15:
                boss.x_velocity = 5
            
            if boss.y >= (screen.get_height()/100)*85:
                boss.y_velocity = -8
            if boss.y <= (screen.get_height()/100)*15:
                boss.y_velocity = 8

            boss.y = boss.y + boss.y_velocity
            boss.x = boss.x + boss.x_velocity

            checkColl = HasCollided(boss.x,boss.y,ship_x,ship_top,105)
            if checkColl == True:
                game_state = 'game over'

        if ship_lives <= 0:
            game_state = 'game over'
        
        score_text_drawer = score_text.render(str(score),True,(255,255,255),None)
        live_text_drawer = score_text.render(str(ship_lives),True,(255,0,0),None)
        screen.blit(score_text_drawer,(0,0))
        screen.blit(live_text_drawer,((screen.get_width()/100)*95,0))
            

    elif game_state == 'game over':
        current_time = 0
        last_time = 0
        asteroids.clear()
        enemies.clear()
        shots.clear()
        m_asteroids.clear()
        fa_enemies.clear()
        bosses.clear()
        score = 0

        screen.fill((0,0,0))
        screen.blit(bg,(0,0))
        font = pygame.font.Font('freesansbold.ttf', 32)
        gameovertext = font.render('Vesztettél!',True,(255,255,255),None)
        restart = font.render('Nyomdd meg a space-t az újrakezdéshez!',True,(255,255,255),None)

        screen.blit(gameovertext,((screen.get_width()/100)*45,(screen.get_height()/100)*60))
        screen.blit(restart,((screen.get_width()/100)*30,(screen.get_height()/100)*20))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    ship_lives = 3
                    game_state = 'game'
                    print(game_state)

    elif game_state == 'game win':

        current_time = 0
        last_time = 0
        asteroids.clear()
        enemies.clear()
        shots.clear()
        m_asteroids.clear()
        fa_enemies.clear()
        bosses.clear()
        score = 0

        screen.fill((0,0,0))
        screen.blit(bg,(0,0))
        font = pygame.font.Font('freesansbold.ttf', 32)
        gameovertext = font.render('Nyertél!',True,(255,255,255),None)
        restart = font.render('Nyomdd meg a space-t az újrakezdéshez!',True,(255,255,255),None)

        screen.blit(gameovertext,((screen.get_width()/100)*45,(screen.get_height()/100)*60))
        screen.blit(restart,((screen.get_width()/100)*30,(screen.get_height()/100)*20))


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    ship_lives = 3
                    game_state = 'game'
                    print(game_state)
    pygame.display.update()

#todo:
#exe legyen a fajl