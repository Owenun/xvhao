import pygame

from pygame.sprite import Sprite

import sys

import random

from pygame.sprite import Group

class Star(Sprite):
    def __init__(self,screen):
        super(Star,self).__init__()
        #星星的图像
        self.image = pygame.image.load("D:/py/2024.3/pygame/Practice4/star_image/star.png")
        self.rect = self.image.get_rect()
        #导入屏幕参数
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #设置星星的位置
        self.rect.x = random.randint(0,1280 - self.rect.width)
        self.rect.y = random.randint(0,720 - self.rect.height)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #星星的移动速度
        self.speed_factor = 0.1
        #星星的初始方向
        direction_value = [-1,1]
        for speed_direction_x in random.sample(direction_value,1):
            self.speed_direction_x = speed_direction_x
        
        for speed_direction_y in random.sample(direction_value,1):
            self.speed_direction_y = speed_direction_y
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.x += self.speed_factor*self.speed_direction_x

        self.y += self.speed_factor*self.speed_direction_y

        self.rect.x = self.x 
        self.rect.y = self.y
    
    def check_edge(self):
        if (self.rect.left == self.screen_rect.left or 
            self.rect.right == self.screen_rect.right):
            self.speed_direction_x *= -1
 
        
        if (self.rect.top == self.screen_rect.top or 
            self.rect.bottom == self.screen_rect.bottom):
            self.speed_direction_y *= -1
        


def check_event(screen,stars):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

            if event.key == pygame.K_SPACE:
                create_new_star(screen,stars)

def create_new_star(screen,stars):
    star = Star(screen)
    stars.add(star)

def star_rand_move():
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("RAND_STAR")
    screen_bg_color = (1,2,3)
    
    stars = Group()
    clock = pygame.time.Clock()
    
    while True:
        check_event(screen,stars)
            
        
        stars.update()
        
        
        screen.fill(screen_bg_color)
        for star in stars:
            star.blitme()
            
            star.check_edge()
        
        pygame.display.flip()
        # clock.tick(120)

star_rand_move()