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

q = True
w = True
o = True
r = True
t = True
y = True
u = True
i = True

q1 = True
w1 = True
o1 = True
r1 = True
t1 = True
y1 = True
u1 = True
i1 = True

q2 = True
w2 = True
o2 = True
r2 = True
t2 = True
y2 = True
u2 = True
i2 = True

fire1 = True
fire2 = False
fire3 = False
fire11 = True
fire21 = False
fire31 = False
fire12 = True
fire22 = False
fire32 = False
fire13 = True
fire23 = False
fire33 = False
fire14 = True
fire24 = False
fire34 = False
fire15 = True
fire25 = False
fire35 = False
fire16 = True
fire26 = False
fire36 = False
fire17 = True
fire27 = False
fire37 = False

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
        bullet = Bullet('пуля1.png.png', self.rect.centerx, self.rect.centery, 5, 1)
        bullets.add(bullet)  
    def fire2(self):
        bullet = Bullet('пуля2.png.png', self.rect.centerx, self.rect.centery, 5, 2)
        bullets.add(bullet)    
    def fire3(self):
        bullet = Bullet('пуля3.png.png', self.rect.centerx, self.rect.centery, 5, 10)
        bullets.add(bullet)   
                 
class Enemy(GameSprite):
    direction = 'down'
    def __init__(self, player_image, player_x, player_y, player_speed, hp):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.hp = hp
    def update(self):
        global missing
        global score
        global balance
        if self.rect.y <= 0:
            self.direction = 'down'
        if self.rect.y >= 550:
            self.rect.y = 0
            missing += 1
            self.rect.x = random.randint(0, 700)
        if self.direction == 'down':
            self.rect.y += self.speed
        collides = sprite.spritecollide(self, bullets, True)
        for c in collides:
            self.hp -= c.damage
        if self.hp < 1:
            self.kill()
            score += 1
            balance += 100
            monster = Enemy('танк1.png.png',random.randint(0, 650), random.randint(-200, -20), random.randint(1,1), 3)
            monsters.add(monster)
class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, damage):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.damage = damage
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

class Boss(GameSprite):
    direction = 'down'
    def __init__(self, player_image, player_x, player_y, player_speed, hp):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.hp = hp
    def update(self):
        global missing
        global score
        global balance
        global finish
        if self.rect.y <= 0:
            self.direction = 'down'
        if self.rect.y >= 550:
            self.rect.y = 0
            missing += 1
            self.rect.x = random.randint(0, 700)
        if self.direction == 'down':
            self.rect.y += 1
        collides = sprite.spritecollide(self, bullets, True)
        for c in collides:
            self.hp -= c.damage
        if self.hp < 1:
            print(self.hp)
            self.kill()
            text4 = font3.render('You win!', True, (255, 215, 0))
            window.blit(text4, (250, 350))
            finish = True
            

class NPS(GameSprite):
    # def update(self):
    #     keys_pressed = key.get_pressed()
    #     if keys_pressed[K_a] and self.rect.x >= 0:
    #         self.rect.x -= self.speed
    #     if keys_pressed[K_d] and self.rect.x <= 650:
            # self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('пуля1.png.png', self.rect.centerx, self.rect.centery, 5, 1)
        bullets.add(bullet)
    def fire2(self):
        bullet = Bullet('пуля2.png.png', self.rect.centerx, self.rect.centery, 5, 2)
        bullets.add(bullet)
    def fire3(self):
        bullet = Bullet('пуля3.png.png', self.rect.centerx, self.rect.centery, 5, 10)
        bullets.add(bullet)
#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale(image.load("поляна.jpg"), (700, 500))

clock = time.Clock()
FPS = 60


monsters = sprite.Group()
for i in range(7):
    monster = Enemy('танк1.png.png',random.randint(0, 650), random.randint(-200, -20), random.randint(1,1), 3)
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
# w4 = Wall(154, 205, 50, 500, 20, 10, 400)





font1 = font.Font(None, 30)
font3 = font.Font(None, 70)
w1 = font1.render('убито-', True, (255, 215, 0))
w2 = font1.render('пропущено-', True, (255, 215, 0))
w3 = font1.render('Баланс-', True, (255, 215, 0))
win = font1.render('You win!', True, (255, 215, 0))
lose = font1.render('You lose!', True, (180, 0, 0))

boss = Boss('танк2.png.png', 350, -20, 1, 3)
bossGroup = sprite.Group(boss)
finish = False
game = True
char_level = 1
spawnboss = False
while game:
    if finish != True:
        window.blit(background, (0, 0))
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        sprite1.reset()
        sprite1.update()
        text1 = font2.render('Счёт:' + str(score), 1, (255, 255, 255))
        text2 = font2.render('Пропущено:' + str(missing), 1, (255, 255, 255))
        text3 = font2.render('Баланс:' + str(balance), 1, (255, 255, 255))
        window.blit(text1, (10, 20))
        window.blit(text2, (10, 50))
        window.blit(text3, (10, 80))
        if missing >= 30:
            text4 = font3.render('You lose!', True, (180, 0, 0))
            window.blit(text4, (250, 350))
            finish = True
    if score >= 200:
        spawnboss = True
        for m in monsters:
            m.kill()
    if spawnboss == True:
        bossGroup.update()
        bossGroup.draw(window)
    sec += 1
    if spawn == True:
        sprite27.reset()
        sprite27.update()
        if sec == 45:
            if fire1 == True:
                sprite27.fire()
            if fire2 == True:
                sprite27.fire2()
            if fire3 == True:
                sprite27.fire3()

    if spawn1 == True:
        sprite2.reset()
        sprite2.update()
        if sec == 45:
            if fire17 == True:
                sprite2.fire()
            if fire27 == True:
                sprite2.fire2()
            if fire37 == True:
                sprite2.fire3()

    if spawn2 == True:
        sprite21.reset()
        sprite21.update()
        if sec == 45:
            if fire11 == True:
                sprite21.fire()
            if fire21 == True:
                sprite21.fire2()
            if fire31 == True:
                sprite21.fire3()

        

    if spawn3 == True:
        sprite22.reset()
        sprite22.update()
        if sec == 45:
            if fire12 == True:
                sprite22.fire()
            if fire22 == True:
                sprite22.fire2()
            if fire32 == True:
                sprite22.fire3()
    if spawn4 == True:
        sprite23.reset()
        sprite23.update()
        if sec == 45:
            if fire13 == True:
                sprite23.fire()
            if fire23 == True:
                sprite23.fire2()
            if fire33 == True:
                sprite23.fire3()
    if spawn5 == True:
        sprite24.reset()
        sprite24.update()
        if sec == 45:
            if fire14 == True:
                sprite24.fire()
            if fire24 == True:
                sprite24.fire2()
            if fire34 == True:
                sprite24.fire3()
    if spawn6 == True:
        sprite25.reset()
        sprite25.update()
        if sec == 45:
            if fire15 == True:
                sprite25.fire()
            if fire25 == True:
                sprite25.fire2()
            if fire35 == True:
                sprite25.fire3()
    if spawn7 == True:
        sprite26.reset()
        sprite26.update()
        if sec == 45:
            if fire16 == True:
                sprite26.fire()
            if fire26 == True:
                sprite26.fire2()
            if fire36 == True:
                sprite26.fire3()
    # if spawn1 == True:
    #     sprite2.reset()
    #     sprite2.update()
    #     if sec == 45:
    #         if fire17 == True:
    #             sprite2.fire()
    #         if fire27 == True:
    #             sprite2.fire2()
    #         if fire37 == True:
    #             sprite2.fire3()
    
    if sec == 45:
        sec = 0
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                if char_level == 1:
                    sprite1.fire()
                if char_level == 2:
                    sprite1.fire2()
                if char_level == 3:
                    sprite1.fire3()

    
            
        if e.type == KEYDOWN:
            if e.unicode == 'z':
                if balance >= 550:
                    balance -= 550
                    char_level = 2
            if e.unicode == 'x':
                if balance >= 1000:
                    balance -= 1000
                    char_level = 3
            if e.unicode == '!' and q1 != False:
                if balance >= 550:
                    balance -= 550
                    fire2 = True
                    fire1 = False
                    q1 = False
            if e.unicode == '@' and w1 != False:
                if balance >= 550:
                    balance -= 550
                    fire27 = True
                    fire17 = False
                    w1 = False
            if e.unicode == '#' and o1 != False:
               if balance >= 550:
                    balance -= 550
                    fire21 = True
                    fire11 = False
                    o1 = False
            if e.unicode == '$' and r1 != False:
                if balance >= 550:
                    balance -= 550
                    fire22 = True
                    fire12 = False
                    r1 = False
            if e.unicode == '%' and t1 != False:
                if balance >= 550:
                    balance -= 550
                    fire23 = True
                    fire13 = False
                    t1 = False
            if e.unicode == '^' and y1 != False:
                if balance >= 550:
                    balance -= 550
                    fire24 = True
                    fire14 = False
                    y1 = False
            if e.unicode == '&' and u1 != False:
                if balance >= 550:
                    balance -= 550
                    fire25 = True
                    fire15 = False
                    u1 = False
            if e.unicode == '*' and i1 != False:
                if balance >= 550:
                    balance -= 550
                    fire26 = True
                    fire16 = False
                    i1 = False


            if e.unicode == 'q' and q2 != False:
                if balance >= 1000:
                    balance -= 1000
                    fire3 = True
                    fire2 = False
                    q2 = False
            if e.unicode == 'w' and w2 != False:
                if balance >= 1000:
                    balance -= 1000
                    fire37 = True
                    fire27 = False
                    w2 = False
            if e.unicode == 'r' and o2 != False:
               if balance >= 1000:
                    balance -= 1000
                    fire31 = True
                    fire21 = False
                    o2 = False
            if e.unicode == 't' and r2 != False:
                if balance >= 1000:
                    balance -= 1000
                    fire32 = True
                    fire22 = False
                    r2 = False
            if e.unicode == 'y' and t2 != False:
                if balance >= 1000:
                    balance -= 1000
                    fire33 = True
                    fire23 = False
                    t2 = False
            if e.unicode == 'u' and y2 != False:
                if balance >= 1000:
                    balance -= 1000
                    fire34 = True
                    fire24 = False
                    y2 = False
            if e.unicode == 'i' and u2 != False:
                if balance >= 550:
                    balance -= 550
                    fire35 = True
                    fire25 = False
                    u2 = False
            if e.unicode == 'o' and i2 != False:
                if balance >= 1000:
                    balance -= 1000
                    fire36 = True
                    fire26 = False
                    i2 = False


            if e.type == KEYDOWN:
                if e.key == K_1:
                    if balance >= 500 and q != False:
                        spawn = True
                        balance -= 500
                        q = False
                if e.key == K_2:
                    if balance >= 500 and w != False:
                        spawn1 = True
                        balance -= 500
                        w = False
                if e.key == K_3:
                    if balance >= 500 and o != False:
                        spawn2 = True
                        balance -= 500
                        o = False
                if e.key == K_4:
                    if balance >= 500 and r != False:
                        spawn3 = True
                        balance -= 500
                        r = False
                if e.key == K_5:
                    if balance >= 500 and t != False:
                        spawn4 = True
                        balance -= 500
                        t = False
                if e.key == K_6:
                    if balance >= 500 and y != False:
                        spawn5 = True
                        balance -= 500
                        y = False
                if e.key == K_7:
                    if balance >= 500 and u != False:
                        spawn6 = True
                        balance -= 500
                        u = False
                if e.key == K_8:
                    if balance >= 500 and i != False:
                        spawn7 = True
                        balance -= 500
                        i = False
            if e.type == KEYDOWN:
                if e.key == K_1:
                    if balance >= 500 and q != False:
                        spawn = True
                        balance -= 500
                        q = False
                if e.key == K_2:
                    if balance >= 500 and w != False:
                        spawn1 = True
                        balance -= 500
                        w = False
                if e.key == K_3:
                    if balance >= 500 and o != False:
                        spawn2 = True
                        balance -= 500
                        o = False
                if e.key == K_4:
                    if balance >= 500 and r != False:
                        spawn3 = True
                        balance -= 500
                        r = False
                if e.key == K_5:
                    if balance >= 500 and t != False:
                        spawn4 = True
                        balance -= 500
                        t = False
                if e.key == K_6:
                    if balance >= 500 and y != False:
                        spawn5 = True
                        balance -= 500
                        y = False
                if e.key == K_7:
                    if balance >= 500 and u != False:
                        spawn6 = True
                        balance -= 500
                        u = False
                if e.key == K_8:
                    if balance >= 500 and i != False:
                        spawn7 = True
                        balance -= 500
                        i = False
                # if e.key == K_2:
                #     if balance >= 500:
                #         spawn1 = True
                #         balance -= 500
    display.update()
    clock.tick(FPS)
