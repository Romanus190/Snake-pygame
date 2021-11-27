import math, time
import pygame as pg
import pygame, random, sys
import numpy as np

global ran
ran = random.randint(0, 10)
ran1 = random.randint(50, 255)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (17, 24, 47)
        # Special thanks to YouTubers Mini - Cafetos and Knivens Beast for raising this issue!
        # Code adjustment courtesy of YouTuber Elija de Hoog
        self.score = 0
        self.speed = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0]+(x*gridsize)) % screen_width), (cur[1]+(y*gridsize)) % screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):#random position of apple
        self.position = (random.randint(0, int(grid_width) - 1) * gridsize, random.randint(0, int(grid_height) - 1) * gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

class Food_Second:
    def __init__(self):
        self.position = (0, 0)
        self.color = (0, 255, 255)#(ran1, ran1, ran1)
        self.randomize_position()

    def randomize_position(self):#random position of apple
        self.position = (random.randint(0, int(grid_width) - 1) * gridsize, random.randint(0, int(grid_height) - 1) * gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

class Food_Third:
    def __init__(self):
        self.position = (0, 0)
        self.color = (ran, ran, ran)
        self.randomize_position_black()

    def randomize_position_black(self):#random position of apple
        self.position = (random.randint(0, int(grid_width) - 1) * gridsize, random.randint(0, int(grid_height) - 1) * gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

class Food_Speed_2:
    def __init__(self):
        self.position = (0, 0)
        self.color = (0, 255, 34)
        self.randomize_position()
        self.speed = 1

    def randomize_position(self):#random position of apple
        self.position = (random.randint(0, int(grid_width) - 1) * gridsize, random.randint(0, int(grid_height) - 1) * gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x+y) % 2 == 0:
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (255, 228, 225), r)
            else:
                rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (245, 245, 245), rr)

screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

def relu(r):
    return r

def upper_speed_x2(speed):
    return math.factorial(speed)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()
    food_2 = Food_Second()
    food_3 = Food_Third()
    food_speed = Food_Speed_2()

    myfont = pygame.font.SysFont("monospace", 16)

    while True:
        clock.tick(4)#speed snake
        snake.handle_keys()

        drawGrid(surface)
        snake.move()

        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()

        if snake.get_head_position() == food_2.position:
            snake.length += 2
            snake.score += 2
            food_2.randomize_position()

        if snake.get_head_position() == food_3.position:
            snake.length = 0
            snake.score = 0
            food_3.randomize_position_black()

            if snake.length == 0:#If the snake eats an apple, then the game is turned off via break
                break

        if snake.get_head_position() == food_speed.position:
            snake.length += 4
            snake.score += 4
            food_speed.randomize_position()

        snake.draw(surface)

        food.draw(surface)
        food_2.draw(surface)
        food_3.draw(surface)
        food_speed.draw(surface)

        screen.blit(surface, (0, 0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0, 0, 0))
        screen.blit(text, (5, 10))
        pygame.display.update()

main()