import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT  # Импорт настроек

class Arena:
    def __init__(self):
        self.background = self.load_background()
        
    def load_background(self):
        """Загружает и масштабирует фоновое изображение"""
        try:
            bg = pygame.image.load("assets/sprites/background.png").convert()
            return pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except Exception as e:
            print(f"Ошибка загрузки фона: {e}")
            # Создаем простой фон, если изображение не загрузилось
            surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            surf.fill((0, 0, 50))  # Темно-синий цвет
            return surf
            
    def draw(self, screen):
        """Отрисовывает фон на экране"""
        screen.blit(self.background, (0, 0))