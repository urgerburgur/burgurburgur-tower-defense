import pygame, sys, time
from pygame.locals import QUIT



pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 300))
pygame.display.set_caption('defend burgur')
DISPLAYSURF.fill((20, 20, 20))
#positionx and positiony
positohogx = 10
positohogy = 10
#base
baseX, baseY = 483, 89
hogbjeovneihnvagkaartlbjrikgknknelth = 100
total_hogbjeovneihnvagkaartlbjrikgknknelth = 100
hpBarBorder = pygame.Rect(baseX, baseY, 102, 20)
hpBar = pygame.Rect(baseX + 1, baseY + 1, 100, 18)
hpFill = pygame.Rect(baseX + 1, baseY + 1, hogbjeovneihnvagkaartlbjrikgknknelth / total_hogbjeovneihnvagkaartlbjrikgknknelth * 100, 18)
manface = pygame.image.load("mandrawing.png")
manface = pygame.transform.smoothscale(manface, (80, 80))

#USEREVENTS
spawnEnemy = pygame.USEREVENT + 1

#this means draw path(its obvious)
def drrvfhudfsdoihbdhshswawrpaithgitigihhihbbvuibihgith():
  pygame.draw.rect(DISPLAYSURF, "sienna3", pygame.rect.Rect(0, 0, 30, 130))
  pygame.draw.rect(DISPLAYSURF, "sienna3", pygame.rect.Rect(30, 100, 170, 30))
  pygame.draw.rect(DISPLAYSURF, "sienna3", pygame.rect.Rect(170, 40, 30, 60))
  pygame.draw.rect(DISPLAYSURF, "sienna3", pygame.rect.Rect(100, 40, 70, 30))
  pygame.draw.rect(DISPLAYSURF, "sienna3", pygame.rect.Rect(100, 70, 30, 130))
  pygame.draw.rect(DISPLAYSURF, "sienna3", pygame.rect.Rect(100, 170, 300, 30))
  pygame.draw.rect(DISPLAYSURF, "sienna3", pygame.rect.Rect(370, 200, 30, 70))
  pygame.draw.rect(DISPLAYSURF, "sienna3", pygame.rect.Rect(310, 240, 60, 30))
  pygame.draw.rect(DISPLAYSURF, "sienna3", pygame.rect.Rect(310, 120, 30, 120))
  pygame.draw.rect(DISPLAYSURF, "sienna3", pygame.rect.Rect(340, 120, 190, 30))
  pygame.draw.rect(DISPLAYSURF, "grey", pygame.rect.Rect(530, 120, 30, 30))
  burugr = pygame.image.load("positohog.png")
  burugr = pygame.transform.scale(burugr, (50, 50))
  DISPLAYSURF.blit(burugr, (523, 110))

Enemies = pygame.sprite.Group()
Sprites = pygame.sprite.Group()

V = pygame.Vector2


#finances
playermony = 2500
font = pygame.font.SysFont("Arial", 30)
pygame.draw.rect(DISPLAYSURF, "white", pygame.rect.Rect(280,50,100,50))
DISPLAYSURF.blit(font.render("$ " + str( playermony), True, "darkgreen"), (285, 60))
#make new class for towers


class towiotuouwotuwohoueyoiurtoyhworeriopoutouwoturoiyeruwoutouers(pygame.sprite.Sprite):
  def __init__(self, financialthings, damage, x, y):
    super().__init__(Sprites)
    self.financialthings = 100
    self.damage = damage
    self.x = x
    self.y = y
    self.projectile = manface
    self.rect = pygame.rect.Rect(0,180,self.x,self.y)
    DISPLAYSURF.blit(font.render("$100", True, "darkgreen"), (0, 190))
  def draw(self):
    pygame.draw.rect(DISPLAYSURF, "white", self.rect)
    DISPLAYSURF.blit(font.render("$100", True, "darkgreen"), (0, 190))
  def update(self):
    self.draw()
  def addtowerererererererererererererererere(self):
    global playermony
    if playermony >= self.financialthings and not wqotgehowehbphweibjqkigroiewhgwbboirebwbgkbklnreerg:
      playermony -= self.financialthings
      tower(self.damage)
      return True
    return False

tower1 = towiotuouwotuwohoueyoiurtoyhworeriopoutouwoturoiyeruwoutouers(100, 10, 80, 50)

    
# define an enemy class to be able to spawn multiple enemies
# inherit the Enemies sprite group -> def an update() func, call Enemies.update() to update all enemies
# move the movement funcs to the enemy class, def attributes e.g. time tick for individual enemy

class tower(pygame.sprite.Sprite):
  def __init__(self, damage):
    super().__init__(Sprites)
    self.image = manface
    self.damage = damage
    self.cd = 1000
    self.lastShot = 1
    self.projectile = manface
    self.placed = False
    self.pos = pygame.mouse.get_pos()
    self.rect = self.image.get_rect(center = self.pos)
  def update(self):
    global wqotgehowehbphweibjqkigroiewhgwbboirebwbgkbklnreerg
    if not self.placed:
      self.pos = pygame.Vector2(pygame.mouse.get_pos())
      self.rect = self.image.get_rect(center = self.pos)
    if self.placed == True and pygame.time.get_ticks() - self.lastShot >= self.cd:
      for enemy in Enemies:
        if self.pos.distance_to(enemy.pos) <= 75:
          enemy.kill()
          self.lastShot = pygame.time.get_ticks()
          break
    DISPLAYSURF.blit(self.image, self.rect)
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        self.placed = True
        wqotgehowehbphweibjqkigroiewhgwbboirebwbgkbklnreerg = False

class enhuhrnbnbnedibigvonnbodjdiobosbndobpkbmy(pygame.sprite.Sprite):
  count = 0
  def __init__(self, speed):
    enhuhrnbnbnedibigvonnbodjdiobosbndobpkbmy.count += 1
    super().__init__(Enemies)
    self.pos = V(positohogx, positohogy)
    self.rect = pygame.Rect(self.pos.x, self.pos.y, 10, 10)
    self.spedvnibofhbonvboihndklnbidnboifoonbiniowwwwwwwwwwwwwwd = speed
    self.starfdyfyhbygvcvnfkhbsihgijbopvjbotttiuevgifbdibimwmwee = time.time()
    self.dirs = ['down', 'right', 'up', 'left', 'down', 'right', 'down', 'left', 'up', 'right']
    self.changedir = [10, 17, 6, 7, 13, 27, 7, 6, 12, 20]
    self.steps = 0
    self.stepepepepspspepepepspsests = 0
  #move enemy
  def moifibvihojbvobiwqvnbinbfrifbvveeneibvihveihgivhenevovnnvimmivienijyup(self):
      self.pos.y -= 10
  def moifibvihojbvobiwqvnbinbfrifbvveeneibvihveihgivhenevovnnvimmivienijydown(self):
      self.pos.y += 10
  def moifibvihojbvobiwqvnbinbfrifbvveeneibvihveihgivhenevovnnvimmivienijyleft(self):
      self.pos.x -= 10
  def moifibvihojbvobiwqvnbinbfrifbvveeneibvihveihgivhenevovnnvimmivienijyright(self):
      self.pos.x += 10
  #draw enemy
  def drrvfhudfsdoihbdhshswawreneibvihveihgivhenevovnnvimmivienijy(self):
    self.rect = pygame.Rect(self.pos.x, self.pos.y, 10, 10)
    pygame.draw.rect(DISPLAYSURF, "firebrick1", self.rect)
  def update(self):
    global hogbjeovneihnvagkaartlbjrikgknknelth
    if self.stepepepepspspepepepspsests == 125:
      hogbjeovneihnvagkaartlbjrikgknknelth -= 5
      self.kill()
    if(time.time() - self.starfdyfyhbygvcvnfkhbsihgijbopvjbotttiuevgifbdibimwmwee > self.spedvnibofhbonvboihndklnbidnboifoonbiniowwwwwwwwwwwwwwd):
      self.starfdyfyhbygvcvnfkhbsihgijbopvjbotttiuevgifbdibimwmwee = time.time()
      self.steps += 1
      self.stepepepepspspepepepspsests += 1
      if self.dirs:
        match self.dirs[0]:
          case 'down':
            self.moifibvihojbvobiwqvnbinbfrifbvveeneibvihveihgivhenevovnnvimmivienijydown()
          case 'up':
            self.moifibvihojbvobiwqvnbinbfrifbvveeneibvihveihgivhenevovnnvimmivienijyup()
          case 'right':
            self.moifibvihojbvobiwqvnbinbfrifbvveeneibvihveihgivhenevovnnvimmivienijyright()
          case 'left':
            self.moifibvihojbvobiwqvnbinbfrifbvveeneibvihveihgivhenevovnnvimmivienijyleft()
    if self.changedir and self.steps == self.changedir[0]:
      self.dirs.pop(0)
      self.changedir.pop(0)
      self.steps = 0
    self.drrvfhudfsdoihbdhshswawreneibvihveihgivhenevovnnvimmivienijy()


#if initalmony >= 100:
  

class totoiyhjojeojporpjeroqwjweokgphjwognonwiwerbitjtojworojhpnmrohtnylnoon(pygame.sprite.Sprite):
  def __init__(self, image):
    pass

t = pygame.time.get_ticks()
clock = pygame.time.Clock()

pygame.time.set_timer(spawnEnemy, 500)

manduhefgubeuigeiusgrf9urgbs9ghdhgerhgf9dbagw0rh0uhewigbeguwhfohgx = 0
manduhefgubeuigeiusgrf9urgbs9ghdhgerhgf9dbagw0rh0uhewigbeguwhfohgy = 220


wqotgehowehbphweibjqkigroiewhgwbboirebwbgkbklnreerg = False # used to select a tower to place
while True:
  events = pygame.event.get()
  clock.tick(60)
  for event in pygame.event.get():
    pos = pygame.mouse.get_pos()
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == spawnEnemy:
      enhuhrnbnbnedibigvonnbodjdiobosbndobpkbmy(0.2)
      if enhuhrnbnbnedibigvonnbodjdiobosbndobpkbmy.count == 10:
        pygame.time.set_timer(spawnEnemy, 0)

    if event.type == pygame.MOUSEBUTTONDOWN:
     if pos[0] >= 0 and pos[0] <= 70:
       if pos[1] >= 230 and pos[1] <= 280:
         if pygame.mouse.get_pressed()[0] and tower1.addtowerererererererererererererererere():
           wqotgehowehbphweibjqkigroiewhgwbboirebwbgkbklnreerg = True
           print("yes")
         else:
           print("no")
    if event.type == pygame.MOUSEBUTTONUP:
      wqotgehowehbphweibjqkigroiewhgwbboirebwbgkbklnreerg = False
      print("clicked")
         
#draw everything
  DISPLAYSURF.fill("black")
  drrvfhudfsdoihbdhshswawrpaithgitigihhihbbvuibihgith()
  Enemies.update()
  Sprites.update()
  # money info
  pygame.draw.rect(DISPLAYSURF, "white", pygame.rect.Rect(280,50,100,50))
  DISPLAYSURF.blit(font.render("$ " + str( playermony), True, "darkgreen"), (285, 60))
  #hp bar
  hpFill = pygame.Rect(baseX + 1, baseY + 1, hogbjeovneihnvagkaartlbjrikgknknelth / total_hogbjeovneihnvagkaartlbjrikgknknelth * 100, 18)
  pygame.draw.rect(DISPLAYSURF, "white", hpBarBorder)
  pygame.draw.rect(DISPLAYSURF, "black", hpBar)
  pygame.draw.rect(DISPLAYSURF, "red3", hpFill)
  DISPLAYSURF.blit(manface, (manduhefgubeuigeiusgrf9urgbs9ghdhgerhgf9dbagw0rh0uhewigbeguwhfohgx, manduhefgubeuigeiusgrf9urgbs9ghdhgerhgf9dbagw0rh0uhewigbeguwhfohgy))
  pygame.display.update()  







