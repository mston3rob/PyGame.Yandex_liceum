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

images_of_meteorites = []
class Meteorite(pygame.sprite.Sprite):

    for i in range(1, 10):
        images_of_meteorites.append(load_image(f'meteor{i}.png'))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(random.choice(images_of_meteorites), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width)
        self.rect.y = random.randint(0, height)

    def update(self):
        pass


for _ in range(10):
    Meteorite(meteorites)

# основной игровой цикл
if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        meteorites.draw(screen)
        meteorites.update()
        pygame.display.flip()
    pygame.quit()