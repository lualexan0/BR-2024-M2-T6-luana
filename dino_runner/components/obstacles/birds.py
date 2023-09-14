import random #gera numeros aleatórios e é usado para escolher aleatoriamente o tipo de passaro

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_WIDTH


class Birds(Obstacle): #bird subclasse da classe obstacle
    def __init__(self, image):
        self.type = random.randint(0, 1) #escolhe aleatoriamente o tipo de passaro
        super().__init__(image, self.type)  #chamando o costrutor da classe obstacle, inicializando bird passando imagem e o tipo escolhido aleatoriamente
        self.rect.y = 245  #alrtura escolhida, caso o dino n agache, ele bate e morre
        self.rect.x = 600  #define posição horizontal

    def update(self, game_speed, obstacles): #atualiza o estado do passaro
        self.rect.x -= game_speed

        if self.rect.right < 0:  # Verifica se o pássaro saiu completamente pela esquerda
            self.reset_position()
    
    def reset_position(self):
        self.rect.x = SCREEN_WIDTH  # Define a posição do pássaro de volta à direita da tela
        self.rect.y = random.randint(200, 300)