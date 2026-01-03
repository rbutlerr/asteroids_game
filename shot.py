import pygame
from constants import SHOT_RADIUS, LINE_WIDTH
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(sef, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(
                surface,
                "white",
                self.position,
                self.radius,
                LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
