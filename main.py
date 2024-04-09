#Создай собственный Шутер!
from pygame import *
import random
import threading

score = 0
missing = 0

sec = 0

font.init()
font2 = font.Font(None, 36)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x <= 650:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('пуля1.png.png', self.rect.centerx, self.rect.centery, 5)
        bullets.add(bullet)        
class Enemy(GameSprite):
    direction = 'down'
    def update(self):
        global missing
        if self.rect.y <= 0:
            self.direction = 'down'
        if self.rect.y >= 550:
            self.rect.y = 0
            missing += 1
            self.rect.x = random.randint(0, 700)
        if self.direction == 'down':
            self.rect.y += self.speed

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

class NPS(GameSprite):
    # def update(self):
    #     keys_pressed = key.get_pressed()
    #     if keys_pressed[K_a] and self.rect.x >= 0:
    #         self.rect.x -= self.speed
    #     if keys_pressed[K_d] and self.rect.x <= 650:
            # self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('пуля1.png.png', self.rect.centerx, self.rect.centery, 5)
        bullets.add(bullet)
#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale(image.load("поляна.jpg"), (700, 500))

clock = time.Clock()
FPS = 60


monsters = sprite.Group()
for i in range(10):
    monster = Enemy('танк1.png.png',random.randint(0, 650), random.randint(-200, -20), random.randint(1,5))
    monsters.add(monster)

bullets = sprite.Group()


sprite1 = Player('пушка1.png.png', 50, 350, 5)
sprite2 = NPS('пушка1.png.png', 50, 400, 5)
sprite21 = NPS('пушка1.png.png', 150, 400, 3)
sprite22 = NPS('пушка1.png.png', 250, 400, 3)
sprite23 = NPS('пушка1.png.png', 350, 400, 3)
sprite24 = NPS('пушка1.png.png', 450, 400, 3)
sprite25 = NPS('пушка1.png.png', 550, 400, 3)
sprite26 = NPS('пушка1.png.png', 650, 400, 3)
# sprite3 = GameSprite('treasure.png', 300, 400, 0)

# w2 = Wall(154, 205, 50, 100, 20, 10, 400)
# w3 = Wall(154, 205, 50, 300, 130, 10, 450)
# w4 = Wall(154, 205, 50, 500, 20, 10, 400)

font.init()
font = font.Font(None, 30)
w1 = font.render('убито-', True, (255, 215, 0))
w2 = font.render('пропущено-', True, (255, 215, 0))
win = font.render('You win!', True, (255, 215, 0))
lose = font.render('You lose!', True, (180, 0, 0))

finish = False
game = True
while game:
    if finish != True:
        window.blit(background, (0, 0))
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy('танк1.png.png',random.randint(0, 650), random.randint(-200, -20), random.randint(1,5))
            monsters.add(monster)
        sprite1.reset()
        sprite1.update()
        # sprite2.reset()
        # sprite2.update()
        # sprite21.reset()
        # sprite21.update()
        # sprite22.reset()
        # sprite22.update()
        # sprite23.reset()
        # sprite23.update()
        # sprite24.reset()
        # sprite24.update()
        # sprite25.reset()
        # sprite25.update()
        # sprite26.reset()
        # sprite26.update()
        text1 = font2.render('Счёт:' + str(score), 1, (255, 255, 255))
        text2 = font2.render('Пропущено:' + str(missing), 1, (255, 255, 255))

        window.blit(text1, (10, 20))
        window.blit(text2, (10, 50))
    sec += 1
    if  score >= 1:
        sprite2.reset()
        sprite2.update()
        if sec == 30:
            sprite2.fire()

    if  score >= 2:
        sprite21.reset()
        sprite21.update()
        if sec == 30:
            sprite21.fire()
    if sec == 30:
        sec = 0
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                sprite1.fire()
    display.update()
    clock.tick(FPS)
