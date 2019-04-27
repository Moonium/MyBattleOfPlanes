"""典型的 pygame 游戏结构"""
# import pygame
#
# pygame.init()
#
# print("游戏的代码……")
#
# pygame.quit()


"""pygame 游戏中的模型都是矩形块"""
# import pygame
#
# hero_rect = pygame.Rect(100, 500, 120, 125)
#
# print("英雄的原点 %d %d" % (hero_rect.x, hero_rect.y))
# print("英雄的尺寸 %d %d" % (hero_rect.width, hero_rect.height))
# print("%d %d" % hero_rect.size)


"""飞机大战预演"""
import pygame
from plane_sprites import *

pygame.init()

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

hero = pygame.image.load('./images/me1.png')
screen.blit(hero, (200, 500))

pygame.display.update()

clock = pygame.time.Clock()

hero_rect = pygame.Rect(200, 500, 102, 126)

enemy = GameSprite('./images/enemy1.png')
enemy1 = GameSprite('./images/enemy1.png', 2)

enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:
    clock.tick(60)

    # event_list = pygame.event.get()
    # if event_list:
    #     print(event_list)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出……")

            pygame.quit()

            exit()

    hero_rect.y -= 1

    if hero_rect.y <= -126:
        hero_rect.y = 700

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    enemy_group.update()

    enemy_group.draw(screen)

    pygame.display.update()

pygame.quit()
