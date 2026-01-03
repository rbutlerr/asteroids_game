import pygame, random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, surface):
        pygame.draw.circle(
            surface,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        rot_vec_pos = self.velocity.rotate(angle)
        rot_vec_neg = self.velocity.rotate(-1*angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(
                self.position[0],
                self.position[1],
                new_radius
            )
        asteroid_two = Asteroid(
                self.position[0],
                self.position[1],
                new_radius
            )
        asteroid_one.velocity = rot_vec_pos * 1.2
        asteroid_two.velocity = rot_vec_neg * 1.2

