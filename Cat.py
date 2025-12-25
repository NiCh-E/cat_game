import pygame

class Cat(pygame.sprite.Sprite):

    def  __init__ (self, x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect.center=(x,y)

    
