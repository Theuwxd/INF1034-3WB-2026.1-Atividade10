import pygame
import sys
import random
from pygame.locals import *

pygame.init()



largura = 1000
altura = 700

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Histogramas Interativos")

fonte = pygame.font.SysFont("arial", 22)
fonte_pequena = pygame.font.SysFont("arial", 18)
fonte_titulo = pygame.font.SysFont("arial", 30, bold=True)

clock = pygame.time.Clock()


# HISTOGRAMA 1

lista1 = []

# A lista vai ate pelo menos 50 numeros 
for i in range(50):
    lista1.append(random.randint(0, 100))

num_cat1 = 5


# HISTOGRAMA 2

lista_estatica = [
    10, 20, 30, 40, 50,
    60, 70, 80, 90, 100
]

# Quantidade aleatória de elementos usados
qtd = random.randint(3, len(lista_estatica))

lista2 = []

for i in range(qtd):
    lista2.append(lista_estatica[i])

num_cat2 = 4



# HISTOGRAMA 3

lista3 = []

num_cat3 = 6

input_texto = ""
digitando = True


# FUNÇÃO PARA CONTAR CATEGORIAS

def contabiliza_totais(nums, num_cat):

    num_min = min(nums)
    num_max = max(nums)

    if num_max == num_min:
        tam_cat = 1
    else:
        tam_cat = (num_max - num_min) / num_cat

    lista_total = [0] * num_cat

    for i in range(len(nums)):

        if nums[i] == num_max:
            lista_total[-1] += 1
            continue

        for i_cat in range(num_cat):

            lim_inf = num_min + i_cat * tam_cat
            lim_sup = lim_inf + tam_cat

            if lim_inf <= nums[i] < lim_sup:
                lista_total[i_cat] += 1
                break

    return lista_total, num_min, tam_cat



# FUNÇÃO PARA GERAR CORES

def gerar_cores(qtd):

    cores = []

    for i in range(qtd):

        cor = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )

        cores.append(cor)

    return cores


cores1 = gerar_cores(num_cat1)
cores2 = gerar_cores(num_cat2)
cores3 = gerar_cores(num_cat3)



# FUNÇÃO PARA DESENHAR HISTOGRAMA

def desenhar_histograma(
        lista,
        num_cat,
        cores,
        titulo
):

    totais, num_min, tam_cat = contabiliza_totais(lista, num_cat)

    screen.fill((20, 20, 20))

    # Título
    texto_titulo = fonte_titulo.render(
        titulo,
        True,
        (255, 255, 255)
    )

    screen.blit(texto_titulo, (300, 40))

    # Instruções
    texto_instrucao = fonte_pequena.render(
        "Seta DIREITA -> próximo | Seta ESQUERDA -> anterior",
        True,
        (255, 255, 255)
    )

    screen.blit(texto_instrucao, (250, 90))

    # EIXOS
    x_base = 120
    y_base = 600

    pygame.draw.line(
        screen,
        (255, 255, 255),
        (x_base, y_base),
        (850, y_base),
        4
    )

    pygame.draw.line(
        screen,
        (255, 255, 255),
        (x_base, y_base),
        (x_base, 150),
        4
    )

    largura_barra = 70
    espacamento = 30

    # Barras
    for i in range(len(totais)):

        altura = totais[i] * 30

        x = x_base + 40 + i * (largura_barra + espacamento)

        y = y_base - altura

        pygame.draw.rect(
            screen,
            cores[i],
            (x, y, largura_barra, altura)
        )

        # Valor no topo
        texto_valor = fonte_pequena.render(
            str(totais[i]),
            True,
            (255, 255, 255)
        )

        screen.blit(texto_valor, (x + 20, y - 25))

        # Faixas eixo X
        faixa = int(num_min + i * tam_cat)

        texto_faixa = fonte_pequena.render(
            str(faixa),
            True,
            (255, 255, 255)
        )

        screen.blit(texto_faixa, (x + 15, y_base + 10))

    # Marcações eixo Y
    for i in range(11):

        y_marca = y_base - i * 30

        pygame.draw.line(
            screen,
            (180, 180, 180),
            (x_base - 5, y_marca),
            (x_base + 5, y_marca),
            2
        )

        texto_y = fonte_pequena.render(
            str(i),
            True,
            (255, 255, 255)
        )

        screen.blit(texto_y, (x_base - 35, y_marca - 10))



# TELA DE INPUT DO PYGAME

def tela_input():

    global input_texto
    global lista3
    global digitando

    while digitando:

        screen.fill((15, 15, 15))

        titulo = fonte_titulo.render(
            "Digite 8 números separados por espaço",
            True,
            (255, 255, 255)
        )

        screen.blit(titulo, (180, 180))

        caixa = pygame.Rect(200, 300, 600, 50)

        pygame.draw.rect(screen, (255, 255, 255), caixa, 2)

        texto = fonte.render(
            input_texto,
            True,
            (255, 255, 255)
        )

        screen.blit(texto, (210, 310))

        aviso = fonte_pequena.render(
            "Exemplo: 10 20 30 40 50 60 70 80",
            True,
            (200, 200, 200)
        )

        screen.blit(aviso, (300, 380))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:

                
                if event.key == K_RETURN:

                    try:

                        numeros = input_texto.split()

                        if len(numeros) == 8:

                            lista3 = []

                            for n in numeros:
                                lista3.append(int(n))

                            digitando = False

                    except:
                        pass

                
                elif event.key == K_BACKSPACE:

                    input_texto = input_texto[:-1]

                else:

                    input_texto += event.unicode



# INPUT DO HISTOGRAMA 3
tela_input()

# CONTROLE DE TELAS
histograma_atual = 0

# LOOP PRINCIPAL

while True:

    # HISTOGRAMA 1
    if histograma_atual == 0:

        desenhar_histograma(
            lista1,
            num_cat1,
            cores1,
            "Histograma 1 - Lista Aleatória"
        )

    # HISTOGRAMA 2
    elif histograma_atual == 1:

        desenhar_histograma(
            lista2,
            num_cat2,
            cores2,
            "Histograma 2 - Lista Estática"
        )

    # HISTOGRAMA 3
    elif histograma_atual == 2:

        desenhar_histograma(
            lista3,
            num_cat3,
            cores3,
            "Histograma 3 - Input do PyGame"
        )

    pygame.display.update()

    
    # EVENTOS
    

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:

            # Próximo histograma
            if event.key == K_RIGHT:

                histograma_atual += 1

                if histograma_atual > 2:
                    histograma_atual = 0

            # Histograma anterior
            if event.key == K_LEFT:

                histograma_atual -= 1

                if histograma_atual < 0:
                    histograma_atual = 2

    clock.tick(60)