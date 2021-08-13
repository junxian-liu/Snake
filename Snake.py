import pygame
import random
from pygame.locals import *


pygame.init()
game_height = 600
game_width = 800
game_board = pygame.display.set_mode((game_width, game_height))

pygame.display.set_caption('Snake Game by Junxian Liu')

# Colors
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 128, 0)

snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

apple = pygame.image.load('apple.png')


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, blue)
    game_board.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_board, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_board.blit(mesg, [250, 250])


def game_loop():
    game_over = False
    game_close = False

    x1 = game_width/2
    y1 = game_height/2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, game_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, game_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            game_board.fill(green)
            message("You Lost! Press Q-Quit or C-Play Again", red)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= game_width or x1 < 0 or y1 >= game_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_board.fill(green)
        game_board.blit(apple, (foodx, foody))
        # pygame.draw.rect(game_board, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(snake_length - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, game_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, game_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
