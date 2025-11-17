import pygame
import random
from constants import *
from circleshape import CircleShape
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, field):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        new_rock1_rotation = self.velocity.rotate(angle)
        new_rock2_rotation = self.velocity.rotate(0-angle)
        new_rock_radius = self.radius-ASTEROID_MIN_RADIUS
        field.spawn(new_rock_radius, self.position, new_rock1_rotation)
        field.spawn(new_rock_radius, self.position, new_rock2_rotation)
