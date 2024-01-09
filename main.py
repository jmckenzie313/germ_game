import copy
import math
import pygame
import random

from board import boards

WIDTH, HEIGHT = 900, 950
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Germ")

BG = pygame.transform.scale(pygame.image.load("bg.png"), (WIDTH, HEIGHT))
OBSTACLES = copy.deepcopy(boards)
PI = math.pi 

PLAYER_WIDTH = 25
PLAYER_HEIGHT = 25

SMALL_GERM_WIDTH = 15
SMALL_GERM_HEIGHT = 15

MED_GERM_WIDTH = 40
MED_GERM_HEIGHT = 40

LARGE_GERM_WIDTH = 60
LARGE_GERM_HEIGHT = 60

VEL = 2

player_image = pygame.transform.scale(pygame.image.load(f'assets/player_images/1.png'), (60, 60))
small_germ_image = pygame.transform.scale(pygame.image.load(f'assets/germ_images/blue.png'), (50, 50))
med_germ_img = pygame.transform.scale(pygame.image.load(f'assets/germ_images/orange.png'), (70, 70))
large_germ_img = pygame.transform.scale(pygame.image.load(f'assets/germ_images/red.png'), (90, 90))

class Germs:
    def __init__(self, name, width, height, is_dead, x, y):
        self.name = name
        self.width = width 
        self.height = height
        self.is_dead = is_dead
        self.x = x
        self.y = y

def draw(player, enemy_1, enemy_2, enemy_3):
    WIN.blit(player_image, (player.x, player.y))
    if not enemy_1.is_dead:
        WIN.blit(small_germ_image, (enemy_1.x, enemy_1.y))
    if not enemy_2.is_dead:
        WIN.blit(med_germ_img, (enemy_2.x, enemy_2.y))
    if not enemy_3.is_dead:
        WIN.blit(large_germ_img, (enemy_3.x, enemy_3.y))

    pygame.display.update()

def draw_obstacles():
        num1 = ((HEIGHT - 50) // 32)
        num2 = (WIDTH // 30)
        for i in range(len(OBSTACLES)):
            for j in range(len(OBSTACLES[i])):
                if OBSTACLES[i][j] == 1:
                    pygame.draw.circle(WIN, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
                if OBSTACLES[i][j] == 2:
                    pygame.draw.circle(WIN, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
                if OBSTACLES[i][j] == 3:
                    pygame.draw.line(WIN, "black", (j * num2 + (0.5 * num2), i * num1),
                                    (j * num2 + (0.5 * num2), i * num1 + num1), 3)
                if OBSTACLES[i][j] == 4:
                    pygame.draw.line(WIN, "black", (j * num2, i * num1 + (0.5 * num1)),
                                    (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
                if OBSTACLES[i][j] == 5:
                    pygame.draw.arc(WIN, "black", [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                    0, PI / 2, 3)
                if OBSTACLES[i][j] == 6:
                    pygame.draw.arc(WIN, "black",
                                    [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
                if OBSTACLES[i][j] == 7:
                    pygame.draw.arc(WIN, "black", [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI,
                                    3 * PI / 2, 3)
                if OBSTACLES[i][j] == 8:
                    pygame.draw.arc(WIN, "black",
                                    [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2,
                                    2 * PI, 3)
                if OBSTACLES[i][j] == 9:
                    pygame.draw.line(WIN, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                    (j * num2 + num2, i * num1 + (0.5 * num1)), 3)


def enemyMove(player, enemy_1, enemy_2, enemy_3):
    enemies = [enemy_1, enemy_2, enemy_3]

    for enemy in enemies:
        direction = random.choice(['left', 'right', 'up', 'down'])
        speed = 0.3

        distance_x = player.x - enemy.x
        distance_y = player.y - enemy.y
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5

        if direction == "up":
            enemy.y -= 1
        elif direction == "down":
            enemy.y += 1
        elif direction == "left":
            enemy.x -= 1
        elif direction == "right":
            enemy.x += 1
        if distance != 0:
            enemy.x += speed * distance_x / distance
            enemy.y += speed * distance_y / distance

            # Check if the enemy is off the WIN
        if enemy.x < 0 or enemy.x > WIDTH or enemy.y < 0 or enemy.y > HEIGHT:
            # If the enemy is off the WIN, reset its position
            enemy.x = random.randint(0, WIDTH)
            enemy.y = random.randint(0, HEIGHT)


def check_collisions(player, enemy_1, enemy_2, enemy_3):
    global player_image
    if ((player.y - player_image.get_height()/2) >= (enemy_1.y - enemy_1.height/2)) and ((player.y - player_image.get_height()/2) <= (enemy_1.y + enemy_1.height/2)) \
        or ((player.y + player_image.get_height()/2) >= (enemy_1.y - enemy_1.height/2)) and ((player.y + player_image.get_height()/2) <= (enemy_1.y + enemy_1.height/2)):
        if ((player.x - player_image.get_width()/2) >= (enemy_1.x - enemy_1.width/2) and (player.x - player_image.get_width()/2) <= (enemy_1.x + enemy_1.width/2)) \
            or ((player.x + player_image.get_width()/2) <= (enemy_1.x + enemy_1.width/2) and (player.x + player_image.get_width()/2) >= (enemy_1.x - enemy_1.width/2)):
            enemy_1.is_dead = True
            player_image = pygame.transform.scale(player_image, (80, 80))
    if ((player.y - player_image.get_height()/2) >= (enemy_2.y - enemy_2.height/2)) and ((player.y - player_image.get_height()/2) <= (enemy_2.y + enemy_2.height/2)) \
        or ((player.y + player_image.get_height()/2) >= (enemy_2.y - enemy_2.height/2)) and ((player.y + player_image.get_height()/2) <= (enemy_2.y + enemy_2.height/2)):
        if ((player.x - player_image.get_width()/2) >= (enemy_2.x - enemy_2.width/2) and (player.x - player_image.get_width()/2) <= (enemy_2.x + enemy_2.width/2)) \
            or ((player.x + player_image.get_width()/2) <= (enemy_2.x + enemy_2.width/2) and (player.x + player_image.get_width()/2) >= (enemy_2.x - enemy_2.width/2)):
            enemy_2.is_dead = True
            player_image = pygame.transform.scale(player_image, (100, 100))
    if ((player.y - player_image.get_height()/2) >= (enemy_3.y - enemy_3.height/2)) and ((player.y - player_image.get_height()/2) <= (enemy_3.y + enemy_3.height/2)) \
        or ((player.y + player_image.get_height()/2) >= (enemy_3.y - enemy_3.height/2)) and ((player.y + player_image.get_height()/2) <= (enemy_3.y + enemy_3.height/2)):
        if ((player.x - player_image.get_width()/2) >= (enemy_3.x - enemy_3.width/2) and (player.x - player_image.get_width()/2) <= (enemy_3.x + enemy_3.width/2)) \
            or ((player.x + player_image.get_width()/2) <= (enemy_3.x + enemy_3.width/2) and (player.x + player_image.get_width()/2) >= (enemy_3.x - enemy_3.width/2)):
            enemy_3.is_dead = True
            player_image = pygame.transform.scale(player_image, (110, 110))


def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    enemy_1 = Germs("enemy_1", small_germ_image.get_width(), small_germ_image.get_height(), False, 500, 500)
    enemy_2 = Germs("enemy_2", med_germ_img.get_width(), med_germ_img.get_height(), False, 500, 200)
    enemy_3 = Germs("enemy_3", large_germ_img.get_width(), large_germ_img.get_height(), False, 750, 300)
    

    while run:
        WIN.fill('white')
        draw_obstacles()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - VEL >= 0:
            player.x -= VEL
        elif keys[pygame.K_RIGHT] and player.x + VEL + player.width <= WIDTH:
            player.x += VEL
        elif keys[pygame.K_UP] and player.y - VEL >= 0:
            player.y -= VEL
        elif keys[pygame.K_DOWN] and player.y + VEL + player.height <= HEIGHT:
            player.y += VEL


        draw(player, enemy_1, enemy_2, enemy_3)
        enemyMove(player, enemy_1, enemy_2, enemy_3)
        check_collisions(player, enemy_1, enemy_2, enemy_3)

        if enemy_1.is_dead and enemy_2.is_dead and enemy_3.is_dead:
            run = False

    pygame.quit()


if __name__ == "__main__":
    main()