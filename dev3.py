# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jettpack Joyride')

# ----- Inicia assets
Barry_WIDTH = 50
Barry_HEIGHT = 38
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('assets/img/.png').convert()
Barry = pygame.image.load('assets/img/.png').convert_alpha()
Barry_small = pygame.transform.scale(Barry, (Barry_WIDTH, Barry_HEIGHT))

# ----- Inicia estruturas de dados
game = True
meteor_x = 200
# y negativo significa que está acima do topo da janela. O meteoro começa fora da janela
meteor_y = -Barry_HEIGHT
meteor_speedx = 3
meteor_speedy = 4

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo
    # Atualizando a posição do meteoro
    meteor_x += meteor_speedx
    meteor_y += meteor_speedy
    # Se o meteoro passar do final da tela, volta para cima
    if meteor_y > HEIGHT or meteor_x + METEOR_WIDTH < 0 or meteor_x > WIDTH:
        meteor_x = 200
        meteor_y = -METEOR_HEIGHT

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    window.blit(Barry_small, (meteor_x, meteor_y))
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados