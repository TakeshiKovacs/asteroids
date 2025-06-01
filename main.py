import pygame
from constants import (
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    PLAYER_RADIUS
)

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updateable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        # Updates are handled in one hit
        updateable.update(dt)
        
        for entity in asteroids:
            if entity.collision(player) == True:
                print("Game over!")
                exit()
        
            for shot in shots:
                if shot.collision(entity) == True:
                    entity.split()
                    shot.kill()
        # We have to draw each thing individually
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        # Limit FPS to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()