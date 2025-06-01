import pygame

from constants import *

from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, position, SHOT_RADIUS):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        
    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius)
    
    def update(self, dt):
        self.position += (self.velocity * dt)