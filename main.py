import pygame
import os
import sys
import random

# инициалитзация pygame для работы со спрайтами и загрузкой изображения
pygame.init()
size = width, height = 1200, 800
screen = pygame.display.set_mode(size)
# инициализация спрайтов метеоритов
meteorites = pygame.sprite.Group()
# список из изображений метеоритов (длинна=9)
images_of_meteorites = []
FPS = 50

# функция загрузки изоражения из папки data
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    # конвертирование изображения для обрезки фона
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Meteorite(pygame.sprite.Sprite):
    for i in range(1, 10):
        images_of_meteorites.append(load_image(f'meteor{i}.png'))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(random.choice(images_of_meteorites), (100, 100))
        self.rect = self.image.get_rect()
        # стартовая пзиция
        self.rect.x = random.randint(0, width)
        self.rect.y = 0
        # скорость
        self.vy = random.randint(300, 800)
        if self.rect.x < width / 2:
            self.vx = random.randint(-(self.rect.left / (height / self.vy)) // 1, ((width - self.rect.right) / (height / self.vy)) // 1)
        else:
            self.vx = random.randint(-(self.rect.left / (height / self.vy)) // 1, ((width - self.rect.right) / (height / self.vy)) // 1)

    def update(self):
        self.rect.x += self.vx * clock.tick(FPS) / 1000
        self.rect.y += self.vy * clock.tick(FPS) / 1000

for i in range(4):
    Meteorite(meteorites)


# основной игровой цикл
if __name__ == '__main__':
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(pygame.Color('Black'))

        meteorites.draw(screen)
        meteorites.update()
        pygame.display.flip()
    pygame.quit()