import pygame
import os
import sys
import random

# инициалитзация pygame для работы со спрайтами и загрузкой изображения
pygame.init()
size = width, height = 1200, 840
# ширина экрана должна быть кратна фреймрету (FPS)
screen = pygame.display.set_mode(size)
# инициализация спрайтов метеоритов
meteorites = pygame.sprite.Group()
# список из изображений метеоритов (длинна=9)
images_of_meteorites = []
FPS = 60
surface = pygame.Surface((width, height))
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


def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    rotated_offset = offset_center_to_pivot.rotate(-angle)

    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    surf.blit(rotated_image, rotated_image_rect)


class Meteorite(pygame.sprite.Sprite):
    for i in range(1, 10):
        images_of_meteorites.append(load_image(f'meteor{i}.png'))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(random.choice(images_of_meteorites), (100, 100))
        self.rect = self.image.get_rect()
        self.angle = 0
        w = self.image.get_size()[0] / 2
        # стартовая пзиция
        self.rect.x = random.randint(0, width)
        self.rect.y = 0
        # скорость
        self.vy = random.randint(3, 5)
        # перемещение методом rect.move() работает не покадрово а за каждый тик (1000 раз в секунду),
        # поэтому указываем скорось в пикселях, деленных на фреймрейт
        self.vx = random.randint(-(((self.rect.left - w) / FPS) / ((height / FPS) / self.vy)) // 1, (((width / FPS) - ((self.rect.right - w) / FPS)) / ((height / FPS) / self.vy)) // 1)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        w, h = self.image.get_size()
        blitRotate(surface, self.image, (self.rect.x, self.rect.y), (w / 2, h / 2), self.angle)
        screen.blit(surface, (0, 0))
        self.angle += 1


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
        surface.fill(pygame.Color('Black'))
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()