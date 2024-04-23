#Создай собственный Шутер!
from pygame import *
import random
import threading

score = 0
missing = 0
balance = 0
sec = 0
spawn = False
spawn2 = False
spawn3 = False
spawn4 = False
spawn5 = False
spawn6 = False
spawn7 = False
spawn1 = False

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
    def fire2(self):
        bullet = Bullet('пуля2.png.png', self.rect.centerx, self.rect.centery, 5)
        bullets.add(bullet)
    def fire3(self):
        bullet = Bullet('пуля3.png.png', self.rect.centerx, self.rect.centery, 5)
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
sprite2 = NPS('пушка1.png.png', 70, 400, 5)
sprite21 = NPS('пушка1.png.png', 150, 400, 3)
sprite22 = NPS('пушка1.png.png', 250, 400, 3)
sprite23 = NPS('пушка1.png.png', 350, 400, 3)
sprite24 = NPS('пушка1.png.png', 450, 400, 3)
sprite25 = NPS('пушка1.png.png', 550, 400, 3)
sprite26 = NPS('пушка1.png.png', 625, 400, 3)
sprite27 = NPS('пушка1.png.png', 0, 400, 5)
#sprite3 = GameSprite('treasure.png', 300, 400, 0)

# w2 = Wall(154, 205, 50, 100, 20, 10, 400)
# w3 = Wall(154, 205, 50, 300, 130, 10, 450)
# w4 = Wall(154, 205, 50, 500, 20, 10, 400)a

font.init()
font = font.Font(None, 30)
w1 = font.render('убито-', True, (255, 215, 0))
w2 = font.render('пропущено-', True, (255, 215, 0))
w3 = font.render('Баланс-', True, (255, 215, 0))
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
            balance += 100
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
        text3 = font2.render('Баланс:' + str(balance), 1, (255, 255, 255))

        window.blit(text1, (10, 20))
        window.blit(text2, (10, 50))
        window.blit(text3, (10, 80))
    sec += 1
    if spawn == True:
        sprite27.reset()
        sprite27.update()
        if sec == 45:
            if 0 <= score <= 500:
                sprite27.fire()
            elif 501 <= score <= 1000:
                sprite27.fire2()
            elif score >= 1001:
                sprite27.fire3()

    if spawn2 == True:
        sprite21.reset()
        sprite21.update()
        if sec == 45:
            if 0 <= score <= 500:
                sprite21.fire()
            elif 501 <= score <= 1000:
                sprite21.fire2()
            elif score >= 1001:
                sprite21.fire3()
        

    if spawn3 == True:
        sprite22.reset()
        sprite22.update()
        if sec == 45:
            if 0 <= score <= 500:
                sprite22.fire()
            elif 501 <= score <= 1000:
                sprite22.fire2()
            elif score >= 1001:
                sprite22.fire3()
    if spawn4 == True:
        sprite23.reset()
        sprite23.update()
        if sec == 45:
            if 0 <= score <= 500:
                sprite23.fire()
            elif 501 <= score <= 1000:
                sprite23.fire2()
            elif score >= 1001:
                sprite23.fire3()
    if spawn5 == True:
        sprite24.reset()
        sprite24.update()
        if sec == 45:
            if 0 <= score <= 500:
                sprite24.fire()  
            elif 501 <= score <= 1000:
                sprite24.fire2()
            elif score >= 1001:
                sprite24.fire3()
    if spawn6 == True:
        sprite25.reset()
        sprite25.update()
        if sec == 45:
            if 0 <= score <= 501:
                sprite25.fire()
            elif 501 <= score <= 1000:
                sprite25.fire2()
            elif score >= 1001:
                sprite25.fire3()
    if spawn7 == True:
        sprite26.reset()
        sprite26.update()
        if sec == 45:
            if 0 <= score <= 500:
                sprite26.fire()
            elif 501 <= score <= 1000:
                sprite26.fire2()
            elif score >= 1001:
                sprite26.fire3()
    if spawn1 == True:
        sprite2.reset()
        sprite2.update()
        if sec == 45:
            if 0 <= score <= 500:
                sprite2.fire()
            elif 501 <= score <= 1000:
                sprite2.fire2()
            elif score >= 1001:
                sprite2.fire3()
    
    if sec == 45:
        sec = 0
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                sprite1.fire()
        if e.type == KEYDOWN:
            if e.key == K_1:
                if balance >= 500:
                    spawn = True
                    balance -= 500
            if e.key == K_3:
                if balance >= 500:
                    spawn2 = True
                    balance -= 500
            if e.key == K_4:
                if balance >= 500:
                    spawn3 = True
                    balance -= 500
            if e.key == K_5:
                if balance >= 500:
                    spawn4 = True
                    balance -= 500
            if e.key == K_6:
                if balance >= 500:
                    spawn5 = True
                    balance -= 500
            if e.key == K_7:
                if balance >= 500:
                    spawn6 = True
                    balance -= 500
            if e.key == K_8:
                if balance >= 500:
                    spawn7 = True
                    balance -= 500
            if e.key == K_2:
                if balance >= 500:
                    spawn1 = True
                    balance -= 500
    display.update()
    clock.tick(FPS)
