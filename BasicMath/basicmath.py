#! /usr/bin/env python

import random
import sys

import pygame

# inicia a game
pygame.init()

# Defini Display
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('BasicMath - Matemática Divertida!')
bg = pygame.image.load("background.jpg")  # carrega fundo

# Defini cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Variaveis Globais
operador = ""
acertos = 0
erros = 0
valor1 = 0
valor2 = 0
resultado = 0
exibeValor1 = 0
exibeValor2 = 0
exibeOperador = 0
exibeResultado = 0
Aproveitamento = 0
segundos = 0
minutos = 0

# Fontes
fonteTitulo = pygame.font.SysFont("Impact", 35)
fonteSubtitulo = pygame.font.SysFont("Impact", 20)
fontevalores = pygame.font.SysFont("Impact", 50)

# Formatacao de objetos na tela
titulo = fonteTitulo.render("BasicMath - Matemática Básica", 1, WHITE)
titulosub = fonteSubtitulo.render("Jogue - Pratique - Aprenda", 1, GREEN)
subTitulo = fonteTitulo.render("Pense e Responda", 1, GREEN)
Alex = fonteSubtitulo.render(str(" @ by Alex "), 1, GREEN)
regra = fonteSubtitulo.render("* Regra: Clique em Jogar e depois no Operador Correto! *", 1, RED)
exibeaproveitamento = fonteSubtitulo.render(str(" Aproveitamento"), 1, GREEN)
doisPontos = fonteSubtitulo.render(str(":"), 1, GREEN)
timerTexto = fonteSubtitulo.render(str(" Timer "), 1, GREEN)

Acertos = fonteSubtitulo.render("Acertos: ", 1, GREEN)
TotalAcertos = fonteSubtitulo.render(str(acertos), 1, WHITE)
Erros = fonteSubtitulo.render("Erros: ", 1, RED)
TotalErros = fonteSubtitulo.render(str(erros), 1, WHITE)

respostaCerta = fonteTitulo.render(str("Acertou !!!"), 1, GREEN)
respostaErrada = fonteTitulo.render(str("Errou !!!"), 1, RED)

SeparaOperacao = fontevalores.render(str(" _ "), 1, RED)
igual = fontevalores.render(str(" = "), 1, RED)
Soma = fontevalores.render(str(" + "), 1, RED)
Subtracao = fontevalores.render(str(" - "), 1, RED)
Multiplicacao = fontevalores.render(str(" x "), 1, RED)
Divisao = fontevalores.render(str(" / "), 1, RED)
respostaCorreta = fonteSubtitulo.render("Resposta Correta:", 1, GREEN)

# carrega botões/imagens
botaoSoma = pygame.image.load("soma.png")
botaoSubtracao = pygame.image.load("subtracao.png")
botaoMultiplicacao = pygame.image.load("multiplicacao.png")
botaDivisao = pygame.image.load("divisao.png")
botaoSair = pygame.image.load("sair.png")
botaoNovoJogo = pygame.image.load("novojogo.png")
botaoResetar = pygame.image.load("resetarJogo.png")

# som com problemass
# pygame.mixer.music.load("pygame.WAV")
# pygame.mixer.music.play(-1)


# controlar a velocidade de atualizacoes da tela
clock = pygame.time.Clock()

# variaveis para controlar mensagem de certo/errado na tela
certo = False
errado = False


# funcao exibir operador correto
def operadorCorreto():
    if (exibeOperador == 1):
        tela.blit(Soma, [80, 495])
    elif (exibeOperador == 2):
        tela.blit(Subtracao, [80, 495])
    elif (exibeOperador == 3):
        tela.blit(Multiplicacao, [80, 495])
    elif (exibeOperador == 4):
        tela.blit(Divisao, [80, 495])


# main loop

while True:
    # programa nao vai rodar a mais que 120fps
    clock.tick(30)

    # limpar tela
    tela.fill(0)

    # exibir na tela
    TotalAcertos = fonteSubtitulo.render(str(acertos), 1, WHITE)
    TotalErros = fonteSubtitulo.render(str(erros), 1, WHITE)

    Valor1 = fontevalores.render(str(valor1), 1, WHITE)
    Valor2 = fontevalores.render(str(valor2), 1, WHITE)
    Resultado = fontevalores.render(str(resultado), 1, GREEN)

    ExibeValor1Certo = fonteTitulo.render(str(exibeValor1), 1, GREEN)
    ExibeValor2Certo = fonteTitulo.render(str(exibeValor2), 1, GREEN)
    ExibeResultado = fonteTitulo.render(str(exibeResultado), 1, GREEN)

    Media = fonteSubtitulo.render(str("{0:.2f}".format(Aproveitamento) + " %"), 1, WHITE)

    tela.blit(bg, [0, 0])
    tela.blit(titulo, (20, 20))
    tela.blit(Alex, (565, 65))
    tela.blit(titulosub, (20, 60))
    tela.blit(subTitulo, (270, 150))

    tela.blit(Acertos, (650, 380))
    tela.blit(TotalAcertos, (730, 380))
    tela.blit(Erros, (650, 410))
    tela.blit(TotalErros, (730, 410))
    tela.blit(Media, (575, 504))

    tela.blit(SeparaOperacao, (320, 250))
    tela.blit(igual, (420, 250))
    tela.blit(regra, (20, 560))

    tela.blit(botaoSoma, [230, 350])
    tela.blit(botaoSubtracao, [310, 350])
    tela.blit(botaoMultiplicacao, [390, 350])
    tela.blit(botaDivisao, [475, 350])
    tela.blit(botaoSair, [690, 550])
    tela.blit(botaoNovoJogo, [20, 260])
    tela.blit(botaoResetar, [570, 550])

    tela.blit(Valor1, [250, 250])
    tela.blit(Valor2, [370, 250])
    tela.blit(Resultado, [460, 250])

    tela.blit(respostaCorreta, [20, 470])
    tela.blit(ExibeValor1Certo, [25, 505])
    tela.blit(ExibeValor2Certo, [120, 505])
    tela.blit(igual, [160, 495])
    tela.blit(ExibeResultado, [200, 505])
    tela.blit(exibeaproveitamento, [650, 504])
    tela.blit(timerTexto, [670, 200])

    pygame.draw.ellipse(tela, BLUE, [560, 30, 100, 100], 4)
    pygame.draw.ellipse(tela, BLUE, [630, 180, 130, 130], 4)
    pygame.draw.ellipse(tela, BLUE, [630, 340, 130, 130], 4)
    pygame.draw.rect(tela, BLUE, [17, 500, 280, 50], 4)
    pygame.draw.rect(tela, BLUE, [570, 500, 220, 30], 4)

    # cronometro
    segundos = int(pygame.time.get_ticks() / 1000)
    seg = segundos % 60
    minu = (segundos // 60) % 60
    hora = (segundos // 60 // 60) % 24
    if (seg < 10):
        segundosFonte = fonteSubtitulo.render(str(hora) + ":0" + str(minu) + ":0" + str(seg), 0, (WHITE))

    if (minu < 10 and seg > 9):
        segundosFonte = fonteSubtitulo.render(str(hora) + ":0" + str(minu) + ":" + str(seg), 0, (WHITE))

    if (minu >= 10 and seg < 10):
        segundosFonte = fonteSubtitulo.render(str(hora) + ":" + str(minu) + ":0" + str(seg), 0, (WHITE))

    if (minu >= 10 and seg > 9):
        segundosFonte = fonteSubtitulo.render(str(hora) + ":" + str(minu) + ":" + str(seg), 0, (WHITE))
    tela.blit(segundosFonte, (670, 240))

    # exibe resposta certa ou errada na tela
    if (certo == True):
        tela.blit(respostaCerta, [330, 430])
    if (errado == True):
        tela.blit(respostaErrada, [330, 430])

    # exibe o operador na tela
    operadorCorreto()

    # update na tela
    pygame.display.flip()

    for event in pygame.event.get():
        # fecha o jogo
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
            sys.end()

        # pegar o click do mouse para verificar acertos

        if (event.type == pygame.MOUSEBUTTONDOWN):

            # pega a posicao do mouse
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]

            # pega click no botao jogar
            if (mouseX >= 20 and mouseX <= 170):
                if (mouseY >= 260 and mouseY <= 320):
                    certo = False
                    errado = False
                    valor1 = random.randint(1, 999)
                    valor2 = random.randint(1, 99)
                    operador = random.randint(1, 4)

                    # Pega valor do operador randomico, e atribui a uma operação
                    if (operador == 1):
                        resultado = valor1 + valor2
                    elif (operador == 2):
                        resultado = valor1 - valor2
                    elif (operador == 3):
                        resultado = valor1 * valor2
                    elif (operador == 4):
                        resultado = int(valor1 / valor2)

                    # zera a resposta
                    exibeValor1 = 0
                    exibeValor2 = 0
                    exibeResultado = 0
                    exibeOperador = ""

            # pega click nos botoes de somar
            if (mouseX >= 250 and mouseX <= 300):
                if (mouseY >= 350 and mouseY <= 400):
                    if (operador == 1):
                        acertos += 1
                        certo = True
                    elif (operador == 2 or operador == 3 or operador == 4):
                        erros += 1
                        errado = True

                    # variaveis para exibir resposta correta na tela
                    exibeValor1 = valor1
                    exibeValor2 = valor2
                    exibeOperador = operador
                    exibeResultado = resultado

                    # zera as variaveis que operam
                    valor1 = 0
                    valor2 = 0
                    resultado = 0
                    operador = 0

            # pega click nos botoes de subtracao
            elif (mouseX >= 330 and mouseX <= 390):
                if (mouseY >= 350 and mouseY <= 405):
                    if (operador == 2):
                        acertos += 1
                        certo = True
                    elif (operador == 1 or operador == 3 or operador == 4):
                        erros += 1
                        errado = True

                # variaveis para exibir resposta correta na tela
                exibeValor1 = valor1
                exibeValor2 = valor2
                exibeOperador = operador
                exibeResultado = resultado

                # zera as variaveis que operam
                valor1 = 0
                valor2 = 0
                resultado = 0
                operador = 0

            # pega click nos botoes de multiplicacao
            elif (mouseX >= 415 and mouseX <= 470):
                if (mouseY >= 350 and mouseY <= 405):
                    if (operador == 3):
                        acertos += 1
                        certo = True
                    elif (operador == 1 or operador == 2 or operador == 4):
                        erros += 1
                        errado = True

                # variaveis para exibir resposta correta na tela
                exibeValor1 = valor1
                exibeValor2 = valor2
                exibeOperador = operador
                exibeResultado = resultado

                # zera as variaveis que operam
                valor1 = 0
                valor2 = 0
                resultado = 0
                operador = 0

            # pega click nos botoes de dividir
            elif (mouseX >= 495 and mouseX <= 555):
                if (mouseY >= 350 and mouseY <= 403):
                    if (operador == 4):
                        acertos += 1
                        certo = True
                    elif (operador == 1 or operador == 2 or operador == 3):
                        erros += 1
                        errado = True

                # variaveis para exibir resposta correta na tela
                exibeValor1 = valor1
                exibeValor2 = valor2
                exibeOperador = operador
                exibeResultado = resultado

                # zera as variaveis que operam
                valor1 = 0
                valor2 = 0
                resultado = 0
                operador = 0

            # calculo aproveitamento
            total = acertos + erros
            if (total > 0):
                Aproveitamento = ((acertos * 100) / total)

            # click no botao resetar
            if (mouseX >= 571 and mouseX <= 670):
                if (mouseY >= 550 and mouseY <= 591):
                    acertos = 0
                    erros = 0
                    valor1 = 0
                    valor2 = 0
                    resultado = 0
                    certo = False
                    errado = False
                    exibeValor1 = 0
                    exibeValor2 = 0
                    exibeResultado = 0
                    operador = 0
                    exibeOperador = 0
                    minutos = 0
                    segundos = 0
                    total = 0
                    Aproveitamento = 0

            # click no botao sair
            if (mouseX >= 690 and mouseX <= 790):
                if (mouseY >= 550 and mouseY <= 590):
                    pygame.quit()
                    sys.exit()
