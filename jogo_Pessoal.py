import pygame
from random import randint

pygame.init()
x = 350  # 520M 180m ideal:350
y = 100
pos_x = 526
pos_y = 800
pos_a = 300
pos_r = 1500
timer = 0
time_s = 0

speed = 10
outro = 12

fundo = pygame.image.load('Tela.png')
carro = pygame.image.load('carro.png')
figurura = pygame.image.load('rr.png')
azul = pygame.image.load('azul.png')
red = pygame.image.load('red.png')

font = pygame.font.SysFont('arial black', 30)
tx = font.render("Time: ", True, (255, 255, 255), {0, 0, 0})
pos_tx = tx.get_rect()
pos_tx.center = 65, 50

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("1° jogo em python")

janela_open = True
while janela_open:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_open = False
    comando = pygame.key.get_pressed()
    if comando[pygame.K_LEFT] and x >= 180:
        x -= speed
    if comando[pygame.K_RIGHT] and x <= 520:
        x += speed

    if x + 80 > pos_x and y + 180 > pos_y:  # direita
        y = 1200

    if x - 80 < pos_x - 340 and y + 180 > pos_a: # esquerda
        y = 1200

    if x + 80 > pos_x - 176 and y + 180 > pos_r and x - 80 < pos_x - 176 and y + 180 > pos_r:
        y = 1200

    if pos_y <= -80:
        pos_y = randint(800, 1000)

    if pos_a <= -80:
        pos_a = randint(1300, 2000)

    if pos_r <= -80:
        pos_r = randint(2300, 3000)

    if timer < 20:
        timer += 1
    else:
        time_s += 1
        tx = font.render("Tempo: " + str(time_s), True, (255, 255, 255), {0, 0, 0})
        timer = 0

    pos_y -= outro
    pos_a -= outro + 5
    pos_r -= outro + 10

    janela.blit(fundo, (0, 0))
    janela.blit(carro, (x, y))
    janela.blit(figurura, (pos_x, pos_y))
    janela.blit(azul, (pos_x - 340, pos_a))
    janela.blit(red, (pos_x - 176, pos_r))
    janela.blit(tx, pos_tx)
    pygame.display.update()

pygame.quit()
