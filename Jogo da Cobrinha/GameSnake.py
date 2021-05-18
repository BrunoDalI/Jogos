import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()

largura_tela = 640
altura_tela = 480

dimenssao = (largura_tela, altura_tela)



# Cores
verdeEscuro = (100, 255, 100)
verdeClaro = (44, 255, 44)
vermelho = (238, 0, 0)
preto = (0,0,0)

# para movimento da cobra
cobra_x = int(largura_tela/2)
cobra_y = int(altura_tela/2)


# posicao aleatoria 
maca_x = randint(40, 600)
maca_y = randint(50, 430)


# musica de fundo do menu
#musica_fundo = pygame.mixer.music.load('musicaMenu.mp3')
#pygame.mixer.music.play(-1)
# musica quando come a maça
musica_comeu = pygame.mixer.Sound('comeu.wav')


# Fonte para mensagem no jogo
fonte = pygame.font.SysFont("hack", 30, True, False)

# aplica o fundo do jogo
Fundo = pygame.image.load('fundo.png')


# inicia a pontuação com 0
pontos = 0

# Cria tela com as dimensoes passadas por largura_tela/altura_tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Crazy Snake')
relogio = pygame.time.Clock()

def desenha_cobra():
    # circulo
    cobra = pygame.draw.circle(tela, (preto), (cobra_x, cobra_y), 20)
    pygame.draw.circle(tela, (verdeClaro), (cobra_x, cobra_y), 18)
    pygame.draw.circle(tela, (vermelho), (cobra_x , cobra_y + 6), 4)
    pygame.draw.circle(tela, (vermelho), (cobra_x , cobra_y -6), 4)

    #pygame.draw.rect(tela,(255,0,0), (x,  y, 40, 40))
    """
    # quadrado
    pygame.draw.rect(tela,(255,0,0), (200, 300, 40, 40))
    # linha
    pygame.draw.line(tela, (255,255,0), (390,0), (390,600), 5)
    """
    return cobra

macaFundo =  pygame.image.load('maca.png')
def desenha_comida():
    maca = pygame.draw.rect(tela, (vermelho), (maca_x, maca_y, 16, 16))
    tela.blit(macaFundo, (maca_x - 19, maca_y - 19))
    return maca
    
def move_cobra(cobra_x, cobra_y):  
    for event in pygame.event.get():
        if event.type == QUIT:
            # para fechar a tela no x
            pygame.quit()
            exit()
        """ Um movimento por vez 
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                x = x - 20
            if event.key == K_RIGHT:
                x = x + 20
            if event.key == K_UP:
                y = y - 20
            if event.key == K_DOWN:
                y = y + 20
        """
        """ Mover enquanto a tecla for pressionado  """
        if pygame.key.get_pressed()[K_a]:
            cobra_x -= 20
        if pygame.key.get_pressed()[K_d]:
            cobra_x += 20
        if pygame.key.get_pressed()[K_w]:
            cobra_y -= 20
        if pygame.key.get_pressed()[K_s]:
            cobra_y += 20


    return cobra_x, cobra_y


def verifica_colisao(a , b):
    if a.colliderect(b):
        x_random = randint(40, 600)
        y_random = randint(50, 430)



lista_cobra = [ ]
comprimento_inicial = 1

#def desenha_corpo_cobra(lista_cobra):
    #for xy in lista_cobra:
        #pygame.draw.circle(tela, (preto), (xy[0], xy[-1]), 20)
        #pygame.draw.circle(tela, (verdeClaro), (cobra_x, cobra_y), 18)
    

# loop do jogo
while True:
    relogio.tick(30)
    tela.blit(Fundo, (0,0))
    mensagem = f'Score: {pontos}'
    text_format = fonte.render(mensagem, False, (255,255,255))
            
    a = desenha_cobra()
    cobra_x, cobra_y = move_cobra(cobra_x, cobra_y)
    b = desenha_comida()
    if a.colliderect(b):
        maca_x = randint(40, 600)
        maca_y = randint(50, 430)
        pontos += 1
        musica_comeu.play()
        comprimento_inicial += 1
        
    lista_cabeca = []
    lista_cabeca.append(cobra_x)
    lista_cabeca.append(cobra_y)
    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
        
    
   # desenha_corpo_cobra(lista_cobra)
    
    

    # Mostra em tela a pontuação do jogador
    tela.blit(text_format, (0,0))
    pygame.display.update()
            







