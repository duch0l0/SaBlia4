import pygame
from arena import Arena
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("SABLIA4")
    clock = pygame.time.Clock()
    
    arena = Arena()  # Создаем арену с фоном
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Отрисовка
        arena.draw(screen)  # Рисуем фон
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()