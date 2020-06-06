import pygame
import random
import time

pygame.init()

# variables
display_width = 800
display_height = 600
block_time = 10
block_size = 10
food_size = 10
fps = 15
font = pygame.font.SysFont(None, 50)
font1 = pygame.font.SysFont(None, 30)
border_x_block = 750
border_y_block = 500
border_x_mini_block = 20
border_y_mini_block = 10

# display showing
wn = pygame.display.set_mode((display_width, display_height))
title = pygame.display.set_caption('GAME')
# color marking
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
text = ' GAME OVER'
text1 = 'Pres C to continue or Q to quit'


def snake(block_size_, snake_list, color):
    for XnY in snake_list:
        pygame.draw.rect(wn, color, (XnY[0], XnY[1], block_size_, block_size_))


def food(x, y):
    pygame.draw.rect(wn, red, (x, y, food_size, food_size))


def massage(msg, msg1, msg2, color, score, color_score):
    msg = font.render(msg, True, color)
    wn.blit(msg, [650 // 2, 200 // 2])
    msg1 = font.render(msg1, True, color)
    wn.blit(msg1, [550 // 2, 500 // 2])
    msg2 = font1.render(msg2, True, color)
    wn.blit(msg2, [500 // 2, 600 // 2])
    score = font.render(score, True, color_score)
    wn.blit(score, [725 // 2, 350 // 2])


def score_screen(score1):
    score1 = font.render('score: ' + score1, True, green)
    wn.blit(score1, [10, 10])


def border(x, y, zx, zy):
    pygame.draw.rect(wn, white, (x, y, border_x_block, border_x_mini_block))
    pygame.draw.rect(wn, white, (x, y, border_y_mini_block, border_y_block))
    pygame.draw.rect(wn, white, (x, zy, border_x_block, border_x_mini_block))
    pygame.draw.rect(wn, white, (zx, y, border_y_mini_block, border_y_block))


def clock(x):
    clock_1 = pygame.time.Clock()
    clock_1.tick(x)


def gameloop():
    running = True
    gameOver = True
    px = display_width // 2
    py = display_height // 2
    px_change = 0
    py_change = 0
    snake_list = []
    snake_length = 1
    score = 00
    borderX = 30
    borderY = 50
    border_barX = 770
    border_barY = 550
    bounces = 5
    color = blue
    fpsinc = 15

    fx = round(random.randrange(borderX + border_y_mini_block, border_barX - food_size) / 10.0) * 10
    fy = round(random.randrange(borderY + border_x_mini_block, border_barY - food_size) / 10.0) * 10

    while running:
        # backGroundColor
        wn.fill(black)
        while not gameOver:
            wn.fill(black)
            massage('You lose', text, text1, red, str(score), green)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameloop()
                    elif event.key == pygame.K_q:
                        gameOver = True
                        running = False

        # exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            # movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameOver = True
                    running = False

                # move to right and left
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    px_change = block_time
                    py_change = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    px_change = -block_time
                    py_change = 0
                elif event.key == pygame.K_p:
                    time.sleep(10)

                # move to up and down
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    py_change = block_time
                    px_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    py_change = -block_time
                    px_change = 0

        # boundaries and end the game
        if px >= border_barX - 5 or px <= borderX + 5 or py <= borderY + 10 or py >= border_barY - 5:
            gameOver = False

        # update position
        py += py_change
        px += px_change

        # food show
        food(fx, fy)

        border(borderX, borderY, border_barX, border_barY)
        # show player

        snake_Head = [px, py]
        snake_list.append(snake_Head)
        snake(block_size, snake_list, color)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for each in snake_list[:-1]:
            if each == snake_Head:
                gameOver = False

        pygame.display.update()
        if px >= fx >= px or px + block_size > fx + food_size > px + block_size:
            if py >= fy >= py or py + block_size > fy + food_size > py + block_size:
                fx = round(random.randrange(borderX + border_y_mini_block, border_barX - food_size) / 10.0) * 10
                fy = round(random.randrange(borderY + border_x_mini_block, border_barY - food_size) / 10.0) * 10
                score += 2
                snake_length += 2
                if len(snake_list) > bounces:
                    bounces *= bounces
                    score += 3
                    color = green
                    fpsinc += 5
                    if len(snake_list) > 20:
                        fpsinc += 10
                        score += 7
                        color = red

        score_screen(str(score))
        pygame.display.update()
        # frame per second
        clock(fpsinc)


gameloop()
