import pygame
import os
pygame.init()
largura = 400
altura = 600
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Meu Jogo")
continuar = True
cinza = (190, 190, 190)
branco = (255, 255, 255)
preto = (0, 0, 0)
test = (25, 80, 101)
largura_faixa = 10
altura_faixa = altura
img_carro = pygame.image.load(os.path.join('image','carro.png'))
while(continuar):
	for event in pygame.event.get():
		print(event)
		if(event.type == pygame.QUIT):
			continuar = False
	tela.fill(test)
	#faixa = pygame.draw.rect(tela,branco,[largura/2,altura/2,50,50])
	faixa = pygame.draw.rect(tela, branco, [largura/2-largura_faixa/2, altura/2-altura_faixa/2, largura_faixa,altura_faixa])
	carro = tela.blit(img_carro,(0,0))
	pygame.display.update()
pygame.quit()
