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

SMALL_GERM_WIDTH = 25
SMALL_GERM_HEIGHT = 25

MED_GERM_WIDTH = 40
MED_GERM_HEIGHT = 40

LARGE_GERM_WIDTH = 60
LARGE_GERM_HEIGHT = 60

VEL = 2

small_germ_dead = False
med_germ_dead = False
large_germ_dead = False

player_image = pygame.transform.scale(pygame.image.load(f'assets/player_images/1.png'), (60, 60))
small_germ_image = pygame.transform.scale(pygame.image.load(f'assets/germ_images/blue.png'), (60, 60))
med_germ_img = pygame.transform.scale(pygame.image.load(f'assets/germ_images/orange.png'), (70, 70))
large_germ_img = pygame.transform.scale(pygame.image.load(f'assets/germ_images/red.png'), (80, 80))

def draw(player, enemy_1, enemy_2, enemy_3):
    WIN.blit(player_image, (player.x, player.y))
    WIN.blit(small_germ_image, (enemy_1.x, enemy_1.y))
    WIN.blit(med_germ_img, (enemy_2.x, enemy_2.y))
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


def enemyMove(enemy_1, enemy_2, enemy_3):
    enemies = [enemy_1, enemy_2, enemy_3]

    for enemy in enemies:
        direction = random.choice(['left', 'right', 'up', 'down'])

        if direction == "up":
            enemy.y -= 1
        elif direction == "down":
            enemy.y += 1
        elif direction == "left":
            enemy.x -= 1
        elif direction == "right":
            enemy.x += 1

            # Check if the enemy is off the WIN
        if enemy.x < 0 or enemy.x > WIDTH or enemy.y < 0 or enemy.y > HEIGHT:
            # If the enemy is off the WIN, reset its position
            enemy.x = random.randint(0, WIDTH)
            enemy.y = random.randint(0, HEIGHT)

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    enemy_1 = pygame.Rect(750, 900, SMALL_GERM_WIDTH, SMALL_GERM_HEIGHT)
    enemy_2 = pygame.Rect(500, 250, MED_GERM_WIDTH, MED_GERM_HEIGHT)
    enemy_3 = pygame.Rect(900, 50, LARGE_GERM_WIDTH, LARGE_GERM_HEIGHT)

    enemies = [enemy_1, enemy_2, enemy_3]

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


        enemyMove(enemy_1, enemy_2, enemy_3)

        draw(player, enemy_1, enemy_2, enemy_3)


        distance_x = player.x - enemy_1.x
        distance_y = player.y - enemy_1.y
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5

        # Move the enemy toward the player
        speed = 2

        for enemy in enemies:

            if distance != 0:
                enemy.x += speed * distance_x / distance
                enemy.y += speed * distance_y / distance

    pygame.quit()


if __name__ == "__main__":
    main()