import random

import pygame

WIDTH = 800 #ancho de ventana 
HEIGHT = 600 #alto de mi ventadna
BLACK = (0, 0, 0) #definicion del color negro
WHITE = (255, 255, 255) #definicion del color blanco

pygame.init() #inicializamos pygame
pygame.mixer.init() #esta linea es para el audio
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #creamos la ventana
pygame.display.set_caption("Shooter") #titulo de la ventana 
clock = pygame.time.Clock()  #creamos el reloj

class Player(pygame.sprite.Sprite): #creamos la clase 
	def __init__(self): #se inicia la clase 
		super().__init__() #se carga la super clase
		self.image = pygame.image.load("assets/player.png").convert() #se  carga la imagen 
		self.image.set_colorkey(BLACK) #se quita el borde negro
		self.rect = self.image.get_rect()  #el cuadro 
		self.rect.centerx = WIDTH // 2 #el ancho de la mitad
		self.rect.bottom = HEIGHT - 10 #la altura a la mitad 
		self.speed_x = 0 #la velocidad con la que se va a mover 

	def update(self): #definir la funcion 
		self.speed_x = 0 #velocidad que sea igual a 0
		keystate = pygame.key.get_pressed() #checar si alguna tecla es precionada
		if keystate[pygame.K_LEFT]: #si la tacla fue precionada izquierda
			self.speed_x = -5  #disminuir mi velocidad en
		if keystate[pygame.K_RIGHT]: #si a tecla fue precionada la derecha 
			self.speed_x = 5  #aumentar mi velocidad en x
		self.rect.x += self.speed_x #aumento de velocidad 
		if self.rect.right > WIDTH: #para que el jugadfor no se salga del lado derecho de los vordes de la ventana 
			self.rect.right = WIDTH 
		if self.rect.left < 0: #para que el jugadfor no se salga del lado izquierdo de los vordes de la ventana
			self.rect.left = 0 

class Meteor(pygame.sprite.Sprite): #definimos la clase meteoro
	def __init__(self): #iniciizamos la clase
		super().__init__() #la super clase
		self.image = pygame.image.load("assets/meteorGrey_med1.png").convert() #igresaos la imagen de nuestro metioro
		self.image.set_colorkey(BLACK) #se quita el borde la imagen 
		self.rect = self.image.get_rect() 
		self.rect.x = random.randrange(WIDTH - self.rect.width) #quermos que aparescan donde sea los ostaculos 
		self.rect.y = random.randrange(-100, -40) #dar un efecto que estan bajando
		self.speedy = random.randrange(1, 10) #que cada meteorito tenga velocidad distinta 
		self.speedx = random.randrange(-5, 5) 

	def update(self): #metodo
		self.rect.x += self.speedx #se anade el eje en x
		self.rect.y += self.speedy #se anade el eje en y
		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 22 : #si el 
			self.rect.x = random.randrange(WIDTH - self.rect.width) #que el meteorito tenga moviento 
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(1, 8)


background = pygame.image.load("assets/background.png").convert() #color de fondo 

all_sprites = pygame.sprite.Group() #almacenar a nuestro jugado 
meteor_list = pygame.sprite.Group() #se crea un grupo para almacenar meteoros 

player = Player()
all_sprites.add(player) #agregar a nuestro jiugador a la lista 


for i in range(8): #se agregan 8 meteoros 
	meteor = Meteor() 
	all_sprites.add(meteor) #se agrega a la lista de sprite
	meteor_list.add(meteor) #se agrega a la lista de meteoros 


running = True #creamos nuestro bucle principal 
while running:
	
	clock.tick(60) #creamos nuestro bucle principal 
	
	for event in pygame.event.get(): #el evento para salir de la ventana
		
		if event.type == pygame.QUIT:
			running = False
		

	all_sprites.update()


	screen.blit(background, [0, 0]) #para que se pinte tu imagen de fondo 
	all_sprites.draw(screen) #dibujamos en pantalla

	pygame.display.flip()

pygame.quit()