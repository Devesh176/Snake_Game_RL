import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()

font = pygame.font.Font('arial.ttf', 25)

class Direction(Enum):
     RIGHT = 1
     LEFT = 2
     UP = 3
     DOWN = 4
    #  UP_RIGHT = 5
    #  UP_LEFT = 6
    #  DOWN_RIGHT = 7
    #  DOWN_LEFT = 8

Point = namedtuple('Point', 'x, y')

Block_size = 20
SPEED = 10
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)


class GameAI:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.reset()
        
    
    def reset(self):
        self.direction = Direction.RIGHT

        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head]

        self.score = 0
        self.food = None
        
        self.obstacle1 = None
        self.obstacle2 = None
        self.obstacle3 = None
        self.obstacle4 = None
        self.obstacle5 = None
        self._place_food()

        self.frame_iteration = 0
         
         

    def _place_food(self):
        x = random.randint(0, (self.w-Block_size )//Block_size)*Block_size
        y = random.randint(0, (self.h-Block_size )//Block_size)*Block_size 
        
        x1 = random.randint(0, (self.w-Block_size )//Block_size)*Block_size
        y1 = random.randint(0, (self.h-Block_size )//Block_size)*Block_size 
        
        x2 = random.randint(0, (self.w-Block_size )//Block_size)*Block_size
        y2 = random.randint(0, (self.h-Block_size )//Block_size)*Block_size 

        x3 = random.randint(0, (self.w-Block_size )//Block_size)*Block_size
        y3 = random.randint(0, (self.h-Block_size )//Block_size)*Block_size 

        x4 = random.randint(0, (self.w-Block_size )//Block_size)*Block_size
        y4 = random.randint(0, (self.h-Block_size )//Block_size)*Block_size 

        x5 = random.randint(0, (self.w-Block_size )//Block_size)*Block_size
        y5 = random.randint(0, (self.h-Block_size )//Block_size)*Block_size 

       

        self.food = Point(x, y)
        self.obstacle1 = Point(x1, y1) 
        self.obstacle2 = Point(x2, y2)
        self.obstacle3 = Point(x3, y3)
        self.obstacle4 = Point(x4, y4)
        self.obstacle5 = Point(x5, y5)

        
        if self.food in self.snake or self.obstacle1 in self.snake or self.obstacle2 in self.snake or self.obstacle3 in self.snake or self.obstacle4 in self.snake or self.obstacle5 in self.snake:
             self._place_food()
             



    def play_step(self, action):
            self.frame_iteration += 1
            # collect user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                # if event.type == pygame.KEYDOWN:
                #      if event.key == pygame.K_LEFT:
                #           self.direction = Direction.LEFT
                #      elif event.key == pygame.K_RIGHT:
                #           self.direction = Direction.RIGHT
                #      elif event.key == pygame.K_UP:
                #           self.direction = Direction.UP
                #      elif event.key == pygame.K_DOWN:
                #           self.direction = Direction.DOWN
                #     #  elif event.key == pygame.K_UP and event.key == pygame.K_RIGHT:
                #     #       self.direction = Direction.UP_RIGHT
                #     #  elif event.key == pygame.K_UP and event.key == pygame.K_LEFT:
                #     #       self.direction = Direction.UP_LEFT
                #     #  elif event.key == pygame.K_DOWN and event.key == pygame.K_RIGHT:
                #     #       self.direction = Direction.DOWN_RIGHT
                #     #  elif event.key == pygame.K_DOWN and event.key == pygame.K_LEFT:
                #     #       self.direction = Direction.DOWN_LEFT

                        


            # move

            self._move(action) #update head
            # self.snake.insert(0, self.head)

            # check if game over
            reward = 0
            game_over = False
            if self.is_collision() or self.frame_iteration > 100*len(self.snake):
                 game_over = True
                 reward = -10
                 return reward, game_over, self.score

            # place new food or just move 

            if self.head == self.food:
                 self.score += 1
                 reward = 10
                 self._place_food()
            

            # upadate ui and clock
            self._update_ui()
            self.clock.tick(SPEED)

            # return game over and score
            # game_over = False
            return reward, game_over, self.score
    
    def is_collision(self, pt=None):
         if pt is None:
             pt = self.head
         if (
            pt.x > self.w - Block_size 
            or pt.x < 0 
            or pt.y > self.h - Block_size 
            or pt.y < 0
            or pt == self.obstacle1
            or pt == self.obstacle2
            or pt == self.obstacle3
            or pt == self.obstacle4
            or pt == self.obstacle5
             
         ):
              return True
         
         return False
         

    
    
    def _update_ui(self):
        self.display.fill(BLACK)
        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, Block_size, Block_size))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))
         
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, Block_size, Block_size))
        pygame.draw.rect(self.display, WHITE, pygame.Rect(self.obstacle1.x, self.obstacle1.y, Block_size, Block_size))
        pygame.draw.rect(self.display, WHITE, pygame.Rect(self.obstacle2.x, self.obstacle2.y, Block_size, Block_size))
        pygame.draw.rect(self.display, WHITE, pygame.Rect(self.obstacle3.x, self.obstacle3.y, Block_size, Block_size))
        pygame.draw.rect(self.display, WHITE, pygame.Rect(self.obstacle4.x, self.obstacle4.y, Block_size, Block_size))
        pygame.draw.rect(self.display, WHITE, pygame.Rect(self.obstacle5.x, self.obstacle5.y, Block_size, Block_size))

        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    def _move(self, action):

        # [stright, right, left]
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)  

        if np.array_equal(action, [1, 0, 0, 0]):
            new_dir = clock_wise[idx] # no change
        elif np.array_equal(action, [0, 1, 0, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx] # right turn 
        elif np.array_equal(action, [0, 0, 1, 0]):
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx] # left turn
        else: # [0, 0, 0, 1]):
            new_dir = clock_wise[(idx - 2) % 4]

        self.direction = new_dir




        
        x = self.head.x
        y = self.head.y

        if self.direction == Direction.RIGHT:
            x += Block_size
        elif self.direction == Direction.LEFT:
            x -= Block_size
        elif self.direction == Direction.UP:
            y -= Block_size
        elif self.direction == Direction.DOWN:
            y += Block_size
        # elif direction == Direction.UP_RIGHT:
        #     x += Block_size
        #     y -= Block_size
        # elif direction == Direction.UP_LEFT:
        #     x -= Block_size
        #     y -= Block_size
        # elif direction == Direction.DOWN_RIGHT:
        #     x += Block_size
        #     y += Block_size
        # elif direction == Direction.DOWN_LEFT:
        #     x -= Block_size
        #     y += Block_size

        new_head = Point(x, y)

        # Update the positions of all snake segments
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i] = self.snake[i - 1]

        self.head = new_head
        self.snake[0] = self.head

         

if __name__ == '__main__':
    game = GameAI()

    while True:
        game_over, score = game.play_step()

        if game_over == True:
             break
        
        # break if game over
    
    print('Final score', score)
    
    pygame.quit()


