import pygame, sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, drawable, updatable)
    
    Player.containers = (updatable, drawable)
    player = Player(
            SCREEN_WIDTH /2,
            SCREEN_HEIGHT /2
    )
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for obj in asteroids:
            for s in shots:
                if obj.collides_with(s):
                    log_event("asteroid_shot")
                    obj.split()
                    s.kill()
                    
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
        for draw_sprite in drawable:
            draw_sprite.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60))/1000

if __name__ == "__main__":
    main()
