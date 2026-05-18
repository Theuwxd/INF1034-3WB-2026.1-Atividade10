import pygame, sys
from pygame.locals import QUIT

nums = [
    100, 120, 140, 160, 150, 200, 190, 110, 115, 125, 135, 170, 130
]

num_cat = 4
num_min = min(nums)
num_max = max(nums)
tam_cat = (num_max - num_min) / num_cat
lista_total = [0] * num_cat

def contabiliza_totais(nums, lista_total):
    for i in range(len(nums)):
        if nums[i] == num_max:
            lista_total[-1] +=1
            continue
        for i_cat in range(num_cat):
            lim_inf = num_min + i_cat *tam_cat
            lim_sup = lim_inf + tam_cat
            if lim_inf <= nums[i] < lim_sup:
                lista_total[i_cat] += 1
                break
    return lista_total

print(contabiliza_totais(nums, lista_total))

def draw(screen):
    screen_h = screen.get_height()
    for i in range(len(lista_total)):
        x = 100 + 1 *50
        h = 20 * lista_total[i]
        pygame.draw.rect(screen, (255,0,0), (x, screen_h - h - 80, 25, h))



lista_nums = [
    100, 120, 140, 160, 150, 200, 190, 110, 115, 125, 135, 170, 130
]

num = int(input('Digite um numero: '))
lista_nums.append(num)

