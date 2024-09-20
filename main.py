import random

import pygame
from pygame.gfxdraw import pixel

pygame.init()
pygame.display.set_caption("Snake")
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# Parametros da cobra
tamanhoQuadrado = 20
velocidadeJogo = 15


def gerarComida():
    comidaX = round(random.randrange(0, largura - tamanhoQuadrado) / 20.0) * 20.0
    comidaY = round(random.randrange(0, altura - tamanhoQuadrado) / 20.0) * 20.0
    return comidaX, comidaY


def desenharComida(tamanho, comidaX, comidaY):
    pygame.draw.rect(tela, verde, [comidaX, comidaY, tamanho, tamanho])


def desenharCobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branco, [pixel[0], pixel[1], tamanho, tamanho])


def desenharPontos(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelho)
    tela.blit(texto, [1, 1])


def selecionarVelocidade(tecla, velocidadeX, velocidadeY):
    if tecla == pygame.K_DOWN and velocidadeY != -tamanhoQuadrado:
        velocidadeX = 0
        velocidadeY = tamanhoQuadrado
    elif tecla == pygame.K_UP and velocidadeY != tamanhoQuadrado:
        velocidadeX = 0
        velocidadeY = -tamanhoQuadrado
    elif tecla == pygame.K_RIGHT and velocidadeX != -tamanhoQuadrado:
        velocidadeX = tamanhoQuadrado
        velocidadeY = 0
    elif tecla == pygame.K_LEFT and velocidadeX != tamanhoQuadrado:
        velocidadeX = -tamanhoQuadrado
        velocidadeY = 0

    return velocidadeX, velocidadeY


def rodarJogo():
    fimJogo = False

    x = largura / 2
    y = altura / 2

    velocidadeX = 0
    velocidadeY = 0

    tamanhoCobra = 1
    pixels = []

    comidaX, comidaY = gerarComida()

    while not fimJogo:

        tela.fill(preto)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fimJogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidadeX, velocidadeY = selecionarVelocidade(
                    evento.key, velocidadeX, velocidadeY
                )

        # Mostrar comida em tela
        desenharComida(tamanhoQuadrado, comidaX, comidaY)

        # Atualizar a posição da cobra (antes de desenhar pfvr)
        if x < 0 or x > largura or y < 0 or y > altura:
            fimJogo = True

        x += velocidadeX
        y += velocidadeY
        # Mostrar cobra (lá ele)
        pixels.append([x, y])
        if len(pixels) > tamanhoCobra:
            del pixels[0]

        # Regra para morte por auto-colisão
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fimJogo = True

        desenharCobra(tamanhoQuadrado, pixels)
        desenharPontos(tamanhoCobra - 1)

        # Atualização de tela
        pygame.display.update()

        # Nova comida
        if x == comidaX and y == comidaY:
            tamanhoCobra += 1
            comidaX, comidaY = gerarComida()

        relogio.tick(velocidadeJogo)


rodarJogo()
