
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 01:21:52 2020

@author: Home PC
"""
import tkinter
from PIL import ImageTk,Image
import mysql.connector

mydb = mysql.connector.connect(
  host="DESKTOP-BCFOUMG",
  user="user2",
  password="1234",
  database='list'
)
print(mydb)
cursor2= mydb.cursor()
c=0
d=0
s=""
s2=""
try:
     # Executing the SQL command
     cursor2.execute("SELECT * FROM scores")
     myresult= cursor2.fetchall()
     mydb.commit()
except:
    # Rolling back in case of error
    mydb.rollback()
for w in myresult:
    c=c+w[1]
        
try:
     # Executing the SQL command
     cursor2.execute("SELECT * FROM scores2")
     myresult2= cursor2.fetchall()
     mydb.commit()
except:
    # Rolling back in case of error
    mydb.rollback()
for w in myresult2:
    d=d+w[1]  
m=len(myresult2)
n=len(myresult) 
for g in range(n-1): 
        for j in range(0, n-g-1):
            if myresult[j][1] < myresult[j+1][1] : 
                myresult[j], myresult[j+1] = myresult[j+1],myresult[j]
for i in range(0,10,1):
    s+= str(myresult[i])+"\n"
    
#orderfix
for g in range(m-1): 
        for j in range(0, m-g-1):
            
            if myresult2[j][1] < myresult2[j+1][1] : 
                myresult2[j], myresult2[j+1] = myresult2[j+1],myresult2[j]    
for i in range(0,10,1):
    s2+= str(myresult2[i])+"\n"    
   
mydb.close()           
window=tkinter.Tk()
def raise_frame(frame):
     frame.tkraise()
window.configure(background="#1fe046",highlightbackground="#1fe046")
window.iconbitmap(r"C:\Users\Home PC\Desktop\CS\future apple\icon.ico")
menupage=tkinter.Frame(window,background="#1fe046")
playmenu=tkinter.Frame(window,background="#1fe046")
helpcause=tkinter.Frame(window,background="#1fe046")
leaderboard=tkinter.Frame(window,background="#1fe046")
cor=tkinter.Frame(window,background="#1fe046")
ear=tkinter.Frame(window,background="#1fe046")
fan=tkinter.Frame(window,background="#1fe046")                  
finalScore =  0
score = 0
game1speed = 1000
game2speed = 1500
def bleh1():
     bleh=enterbox.get()
     return bleh
#function for the corona game
def asmaan():
    import pygame
    import random
    mydb = mysql.connector.connect(
      host = "DESKTOP-BCFOUMG",
      user = "user2",
      password = "1234",
      database = 'list'
    )
    print(mydb)
    cursor1 = mydb.cursor()
    
    def scoreadder():
        global finalScore  
        try:
           # Executing the SQL command
           cursor1.execute("INSERT INTO scores(username,score) VALUE('"+ bleh1()+"',"+str(int(score))+")")
       
       # Commit your changes in the database
           mydb.commit()
    
        except:
           # Rolling back in case of error
           mydb.rollback()
           mydb.close()
   
    
    def Game1():
    
        global score
        global game1speed
    
        pygame.init()
    
        screen = pygame.display.set_mode((870, 540))
        pygame.display.set_caption("Game 1")
    
        bg = pygame.image.load("Starter.png")
        game1aim = pygame.image.load("game1aim.png")
        sanitizer = pygame.image.load("Sanitizer.png")
        youlose = pygame.image.load("youlose1.png")
        youwin = pygame.image.load("youwin1.png")
    
        font1 = pygame.font.SysFont("comicsansms", 60, True)
        font2 = pygame.font.SysFont("comicsansms", 80, True)
        running = True
    
        class virus(object):
    
            image = pygame.image.load("Virus.png")
    
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.hitbox = (self.x + 10, self.y + 10, 60, 60)
                self.alive = True
    
            def draw(self):
                if self.alive:
                    screen.blit(self.image, (self.x, self.y))
                    self.hitbox = (self.x + 10, self.y + 10, 60, 60)
                    # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 4)
    
            def hit(self):
                self.alive = False
    
        def start():
            l = []
            for i in range(20):
                x = random.randint(440, 680)
                y = random.randint(120, 360)
                l.append(virus(x, y))
            return l
    
        viruses = start()
    
        def redrawGameWindow():
            screen.blit(bg, (0, 0))
            for i in viruses:
                i.draw()
            x, y = pygame.mouse.get_pos()
            screen.blit(sanitizer, (x, y))
            text = font1.render("Time left: " + str(seconds), 1, (0, 0, 0))
            screen.blit(text, (0, 0))
            pygame.display.update()
    
        def lost():
            screen.blit(youlose, (0, 0))
    
            text = font2.render("Score: " + str(score), 1, (255, 255, 255))
            screen.blit(text, (170, 200))
    
            pygame.draw.rect(screen, (255, 100, 10), [300, 380, 220, 100])
            f = font1.render("Quit", 1, (0, 0, 0))
            screen.blit(f, (340, 385))
    
            pygame.display.update()
    
        def won():
            screen.blit(youwin, (0, 0))
    
            text = font2.render("Score: " + str(score), 1, (255, 255, 255))
            screen.blit(text, (200, 200))
    
            pygame.draw.rect(screen, (255, 100, 10), [60, 380, 380, 100])
            f = font1.render("Next game", 1, (0, 0, 0))
            screen.blit(f, (85, 385))
    
            pygame.draw.rect(screen, (255, 100, 10), [540, 380, 220, 100])
            f = font1.render("Quit", 1, (0, 0, 0))
            screen.blit(f, (580, 385))
    
            pygame.display.update()
    
        def aim():
            screen.blit(game1aim, (0, 0))
            pygame.draw.rect(screen, (255, 100, 10), [260, 380, 320, 100])
            f = font1.render("Play game", 1, (0, 0, 0))
            screen.blit(f, (275, 385))
            pygame.display.update()
    
        gameinplay = False
        gamelost = False
        gamewon = False
    
        while running:
    
            if not gameinplay and not gamelost and not gamewon:
    
                aim()
    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
    
                        if 260 < pos[0] < 580 and 380 < pos[1] < 480:
                            gameinplay = True
                            start_ticks = pygame.time.get_ticks()
                            start = pygame.time.get_ticks()
    
            if gamelost:
                lost()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if 300 < pos[0] < 520 and 380 < pos[1] < 480:
                            scoreadder()
                            pygame.quit()
    
            if gamewon:
                won()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if 540 < pos[0] < 760 and 380 < pos[1] < 480:
                            scoreadder()
                            pygame.quit()
                        elif 60 < pos[0] < 440 and 380 < pos[1] < 480:
                            Game2()
    
            if gameinplay:
                counter = len(viruses)
    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        for v in viruses:
                            if v.hitbox[1] + v.hitbox[3] > pos[1] > v.hitbox[1]:
                                if v.hitbox[0] < pos[0] < v.hitbox[0] + v.hitbox[2]:
                                    v.hit()
                                    viruses.pop(viruses.index(v))
                                    score += 10
                                    break
    
                seconds = 20 - (pygame.time.get_ticks() - start_ticks) // 1000
    
                if 20 >= seconds > 3:
                    now = pygame.time.get_ticks()
                    if now - start > game1speed:
                        start = now
                        x = random.randint(422, 707)
                        y = random.randint(108, 399)
                        viruses.append(virus(x, y))
    
                if seconds == 0:
                    gameinplay = False
                    if counter > 0:
                        gamelost = True
                        game1speed = game1speed * 0.9
                    else:
                        gamewon = True
                else:
                    redrawGameWindow()
    
    def Game2():
    
        global score
        global game2speed
    
        rppl = ["person1.png", "person2.png", "person3.png", "person4.png", "person5.png", "person6.png", "person7.png", "person8.png"]
    
        lppl = ["person1flip.png", "person2flip.png", "person3flip.png", "person4flip.png", "person5flip.png", "person6flip.png", "person7flip.png", "person8flip.png"]
    
        miniscore = 0
    
        clock = pygame.time.Clock()
    
        pygame.init()
    
        screen = pygame.display.set_mode((870, 540))
        pygame.display.set_caption("Game 2")
    
        bg = pygame.image.load("woodenfloor.png")
        youlose = pygame.image.load("youlose2.png")
        youwin = pygame.image.load("youwin2.png")
        game2aim = pygame.image.load("game2aim.png")
    
        font1 = pygame.font.SysFont("comicsansms", 60, True)
        font2 = pygame.font.SysFont("comicsansms", 80, True)
        running = True
    
        class player(object):
    
            def __init__(self, x, y, right):
                self.x = x
                self.y = y
                self.vel = 3
                self.path = [10, 850]
                self.right = right
                self.clicked = False
                self.walkCount = 0
                self.hitboxmove = (self.x, self.y, 60, 100)
                self.hitboxgame = (self.x - 20, self.y - 20, 100, 140)
    
                if self.right:
                    self.image = pygame.image.load(random.choice(rppl))
                else:
                    self.image = pygame.image.load(random.choice(lppl))
    
            def move(self):
                if self.right:
                    self.x += self.vel
    
                else:
                    self.x -= self.vel
    
            def draw(self):
                screen.blit(self.image, (self.x, self.y))
                self.hitboxmove = (self.x, self.y, 60, 100)
                self.hitboxgame = (self.x - 20, self.y - 20, 100, 140)
                pygame.draw.rect(screen, (255, 255, 255), self.hitboxgame, 4)
    #            pygame.draw.rect(screen, (0, 255, 255), self.hitboxmove, 4)
    
        people = []
    
        def redrawGameWindow():
            screen.blit(bg, (0, 0))
    
            for i in people:
                i.draw()
    
            text = font1.render("Time left: " + str(seconds), 1, (255, 255, 255))
            screen.blit(text, (0, 0))
    
            pygame.display.update()
    
        def lost():
            global score
            screen.blit(youlose, (0, 0))
    
            text = font2.render("Score: " + str(score), 1, (255, 255, 255))
            screen.blit(text, (170, 200))
    
            pygame.draw.rect(screen, (255, 100, 10), [300, 380, 220, 100])
            f = font1.render("Quit", 1, (0, 0, 0))
            screen.blit(f, (340, 385))
    
            pygame.display.update()
    
        def won():
            global score
            screen.blit(youwin, (0, 0))
    
            text = font2.render("Score: " + str(score), 1, (255, 255, 255))
            screen.blit(text, (200, 200))
    
            pygame.draw.rect(screen, (255, 100, 10), [60, 380, 380, 100])
            f = font1.render("Next game", 1, (0, 0, 0))
            screen.blit(f, (85, 385))
    
            pygame.draw.rect(screen, (255, 100, 10), [540, 380, 220, 100])
            f = font1.render("Quit", 1, (0, 0, 0))
            screen.blit(f, (580, 385))
    
            pygame.display.update()
    
        def aim():
            screen.blit(game2aim, (0, 0))
            pygame.draw.rect(screen, (255, 100, 10), [260, 380, 320, 100])
            f = font1.render("Play game", 1, (0, 0, 0))
            screen.blit(f, (275, 385))
            pygame.display.update()
    
        gameinplay = False
        gamelost = False
        gamewon = False
    
        while running:
            clock.tick(64)
    
            if not gameinplay and not gamelost and not gamewon:
    
                aim()
    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
    
                        if 260 < pos[0] < 580 and 380 < pos[1] < 480:
                            gameinplay = True
                            start_ticks = pygame.time.get_ticks()
                            start = pygame.time.get_ticks()
    
            if gameinplay:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
    
                        for person in people:
                            if person.hitboxmove[1] + person.hitboxmove[3] > pos[1] > person.hitboxmove[1]:
                                if person.hitboxmove[0] < pos[0] < person.hitboxmove[0] + person.hitboxmove[2]:
                                    person.clicked = True
    
                    if event.type == pygame.MOUSEBUTTONUP:
                        for person in people:
                            person.clicked = False
    
                for person in people:
    
                    if not person.clicked and -1 < person.x < 871:
                        person.move()
                    elif person.clicked:
                        pos = pygame.mouse.get_pos()
                        person.x = pos[0]
                        if pos[1] < 140:
                            person.y = 24
                        elif 140 < pos[1] < 436:
                            person.y = pos[1]
                        else:
                            person.y = 416
                    else:
                        people.pop(people.index(person))
                        miniscore += 30
    
                for a in people:
                    for b in people:
                        if a == b:
                            pass
                        else:
                            if a.hitboxgame[1] < b.hitboxgame[1] + b.hitboxgame[3] and a.hitboxgame[1] + a.hitboxgame[3] > b.hitboxgame[1]:
                                if a.hitboxgame[0] + a.hitboxgame[2] > b.hitboxgame[0] and a.hitboxgame[0] < b.hitboxgame[0] + b.hitboxgame[2]:
                                    pygame.time.delay(1000)
                                    gameinplay = False
                                    gamelost = True
                                    score += miniscore
    
                seconds = 15 - (pygame.time.get_ticks() - start_ticks) // 1000
    
                if 15 > seconds > 3:
                    now = pygame.time.get_ticks()
                    if now - start > game2speed:
                        start = now
                        l = [True, False]
                        c = random.choice(l)
                        if c:
                            people.append(player(20, random.randint(120, 440), c))
                        else:
                            people.append(player(850, random.randint(120, 440), c))
    
                if seconds == 0:
                    gameinplay = False
                    gamewon = True
                    game2speed = game2speed * 0.9
                    score += 500
                else:
                    redrawGameWindow()
    
            if gamewon:
                won()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if 540 < pos[0] < 760 and 380 < pos[1] < 480:
                            scoreadder()
                            pygame.quit()
                        elif 60 < pos[0] < 440 and 380 < pos[1] < 480:
                            Game1()
    
            if gamelost:
                lost()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if 300 < pos[0] < 520 and 380 < pos[1] < 480:
                            scoreadder()
                            pygame.quit()
    
    Game1()
#function for the save earth games
def zameen():
    treeGameOn = False
    koalaGameOn = False
    import random
    import pygame
    import mysql.connector
    
    
    mydb = mysql.connector.connect(
      host = "DESKTOP-BCFOUMG",
      user = "user2",
      password = "1234",
      database = 'list'
    )
    print(mydb)
    cursor1 = mydb.cursor()
    
    def scoreadder(scorezz):
        global finalScore  
        try:
           # Executing the SQL command
           cursor1.execute("INSERT INTO scores2(username,score) VALUE('"+bleh1()+"',"+str(int(scorezz))+")")
       
       # Commit your changes in the database
           mydb.commit()
    
        except:
           # Rolling back in case of error
           mydb.rollback()
           mydb.close()
    
    
    def treeGame():
        global finalScore
        nonlocal treeGameOn
        nonlocal koalaGameOn
        treeGameOn = True
        import pygame
        import random
        pygame.init()
        
        #x = min 25 max = 621 length = 596
        #y = max 300 min -50
        y = 125
        x = 298
        score = 5000
        timeTaken = 0
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        window = pygame.display.set_mode((750, 750))
        bg = pygame.image.load("bg2-01.png")
        evil = pygame.image.load("workers-01.png")
        ladyTree = pygame.image.load("ladytree-01.png")
        barHolder = pygame.image.load("bar-01.png")
        keyQ = pygame.image.load("key-01.png")
        keyA = pygame.image.load("keyPressed-01.png")
        lostScreen = pygame.image.load("loseScreen-01.png")
        blackScreen = pygame.image.load("black.png")
        pygame.display.set_caption("Game 2")
        gamePlaying = False
        guessing = True
        keyPressed = ""
        won = False
        lost = False
        
        font = pygame.font.SysFont("comicsansms", 60, True)
        font2 = pygame.font.SysFont("comicsansms", 45, True)
        font3 = pygame.font.SysFont("comicsansms", 20, True)
        font4 = pygame.font.SysFont("comicsansms", 35, True)
        font5 = pygame.font.SysFont("comicsansms", 60, True)
        font6 = pygame.font.SysFont("comicsansms", 30, True)
        
        def win():
            nonlocal score
            window.blit(blackScreen, (0, 0))
            winText = font.render("YOU WIN!", 1, (255, 255, 255))
            window.blit(winText, (225, 275))
            winText2 = font2.render("You saved the tree!", 1, (255, 255, 255))
            window.blit(winText2, (170, 340))
            pygame.draw.rect(window, (255,100,10), pygame.Rect(125, 625, 200, 75)) #original 275
            winText3 = font4.render("Quit", 1, (0, 0, 0))
            window.blit(winText3, (180, 635)) #original 330
            if score > 0:
                winText4 = font4.render("Your score: " + str(int(score)), 1, (255, 255, 255))    
            else:
                winText4 = font4.render("Your score: 100", 1, (255, 255, 255))
            window.blit(winText4, (230, 400))
            
            pygame.draw.rect(window, (255,100,10), pygame.Rect(375, 625, 200, 75))
            winText5 = font6.render("Next Game", 1, (0, 0, 0))
            window.blit(winText5, (390, 640))
            
        def lose():
            window.blit(lostScreen, (0, 0))
            window.blit(blackScreen, (0, 0))
            loseText = font.render("YOU LOSE!", 1, (255, 255, 255))
            window.blit(loseText, (225, 275))
            loseText2 = font3.render("You couldn't save the tree from the wood cutters!", 1, (255, 255, 255))
            window.blit(loseText2, (125, 350))
            pygame.draw.rect(window, (255,100,10), pygame.Rect(125, 625, 200, 75)) #original 275
            winText3 = font4.render("Quit", 1, (0, 0, 0))
            window.blit(winText3, (180, 635)) #original 330
            winText4 = font4.render("Your score: 100", 1, (255, 255, 255))
            window.blit(winText4, (230, 400))
            pygame.draw.rect(window, (255,100,10), pygame.Rect(375, 625, 200, 75))
            winText5 = font6.render("Next Game", 1, (0, 0, 0))
            window.blit(winText5, (390, 640))
        
        run = True
        while run:
            while gamePlaying == False:
                window.blit(bg, (0, 0))
                window.blit(ladyTree, (-100, 50))
                window.blit(barHolder, (0, 0))
                pygame.draw.rect(window, (255,100,10), pygame.Rect(64, 628, x, 82))
                comment = font3.render("Press the key on the keyboard to hug the tree!", 1, (0, 0, 0))
                window.blit(comment, (160, 260))
                window.blit(evil, (y, 100))
                window.blit(blackScreen, (0, 0))
                pygame.draw.rect(window, (255,100,10), pygame.Rect(275, 625, 200, 75))
                text = font4.render("Play Game", 1, (0, 0, 0))
                window.blit(text, (285, 635))
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        treeGameOn = False
                        pygame.quit()
                    if (event.type == pygame.MOUSEBUTTONDOWN):
                        if pygame.mouse.get_pos()[0] in range(275, 475) and pygame.mouse.get_pos()[1] in range(625, 700):
                            startingPoint = pygame.time.get_ticks()
                            gamePlaying = True
                pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    treeGameOn = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    keyPressed = pygame.key.name(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if (won or lost):
                        if pos[0] in range(125, 325) and pos[1] in range(625, 700):
                            treeGameOn = False
                            run = False
                        elif pos[0] in range(375, 575) and pos[1] in range(625, 700):
                            treeGameOn = False
                            koalaGameOn = True
                            run = False
                           #pygame.quit()
                            
            window.blit(bg, (0, 0))
            if (won != True and lost != True):
                window.blit(evil, (y, 100))
                x-= 1.3
                y -= 0.8
                timeTaken = (pygame.time.get_ticks() - startingPoint) / 1000
                score -= timeTaken * 5
            if (won or (won != True and lost != True)):
                window.blit(ladyTree, (-100, 50))
            window.blit(barHolder, (0, 0))
            pygame.draw.rect(window, (255,100,10), pygame.Rect(64, 628, x, 82))
            
            comment = font3.render("Press the key on the keyboard to hug the tree!", 1, (0, 0, 0))
            window.blit(comment, (160, 260))
            
            if guessing:
                letter = random.choice(letters)
                guessing = False
                waiting = True
                
            if waiting:
                window.blit(keyQ, (0, 0))
                qText = font5.render(letter, 1, (0, 0, 0))
                window.blit(qText, (355, 110))
            
            if keyPressed.upper() == letter:
                window.blit(keyA, (0, 0))
                x += 75
                y += 60
                waiting = False
                guessing = True
                
            if x >= 621:
                x = 621
                won = True
                win()
            
            if x <= 0:
                x = 0
                lost = True
                lose()
            
            if lost:
                score = 100
            
            pygame.display.update()
        finalScore += score
            
    def koalaGame():
        global finalScore
        nonlocal koalaGameOn
        nonlocal treeGameOn
        koalaGameOn = True
        import pygame
        import random
        pygame.init()
        
        score_1 = 5000
        coordinatesX = [0, 75, 290, 400, 525, 600]
        coordinatesRangeY = [0, 350]
        win = pygame.display.set_mode((750, 750))
        pygame.display.set_caption("Game 1")
        bg_1 = pygame.image.load("bg-01.png")
        koalaz = pygame.image.load("koala-01.png")
        blackScreen_1 = pygame.image.load("black.png")
        fireClicked = False
        firesBlownOut = 0
        won_1 = False
        lost_1 = False
        gamePlaying_1 = False
        
        font_1 = pygame.font.SysFont("comicsansms", 60, True)
        font_12 = pygame.font.SysFont("comicsansms", 45, True)
        font_13 = pygame.font.SysFont("comicsansms", 20, True)
        font_14 = pygame.font.SysFont("comicsansms", 35, True)
        font6 = pygame.font.SysFont("comicsansms", 30, True)
        
        class koala(object):
            image = pygame.image.load("koala-01.png")
            
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.hitbox = (self.x, self.y, 165, 175)
                self.alive = True
                self.rect = pygame.Rect(self.x, self.y, 165, 175)
                
            def draw(self):
                if self.alive:
                    win.blit(self.image, (self.x, self.y))
                    self.hitbox = (self.x, self.y, 165, 175)
                   # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 3)
                    
        
        class fire(object):
            image = pygame.image.load("fire-02.png").convert_alpha()
            
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.hitbox = (self.x + 25, self.y + 40, 55, 65)
                self.alive = True
                self.rect = pygame.Rect(self.x + 25, self.y + 40, 55, 65)
                
            def drawz(self):
                if self.alive:
                    win.blit(self.image, (self.x, self.y))
                    self.hitbox = (self.x + 25, self.y + 40, 46, 57)
                   # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
            
            def hit(self):
                self.alive = False
                
        def start():
            l = []
            for i in range(200):
                x = random.randrange(0, 675, 25)
                y = random.randrange(-25, 500, 15)
                l.append(fire(x, y))
            return l
        
        fires = start()
        
        def makeKoala():
            x = random.choice(coordinatesX)
            y = random.randrange(0, 350)
            
            return koala(x, y)
        
        koalazzz = makeKoala()
        
        def winz():
            nonlocal score_1
            win.blit(blackScreen_1, (0, 0))
            winText = font_1.render("YOU WIN!", 1, (255, 255, 255))
            win.blit(winText, (225, 275))
            winText2 = font_12.render("You saved the koala!", 1, (255, 255, 255))
            win.blit(winText2, (170, 340))
            pygame.draw.rect(win, (255,100,10), pygame.Rect(125, 625, 200, 75)) #original 275
            winText3 = font_14.render("Quit", 1, (0, 0, 0))
            win.blit(winText3, (180, 635)) #original 330
            if score_1 > 0:
                winText4 = font_14.render("Your score: " + str(int(score_1)), 1, (255, 255, 255))    
            else:
                winText4 = font_14.render("Your score: 100", 1, (255, 255, 255))
            win.blit(winText4, (230, 400))
            pygame.draw.rect(win, (255,100,10), pygame.Rect(375, 625, 200, 75))
            winText5 = font6.render("Next Game", 1, (0, 0, 0))
            win.blit(winText5, (390, 640))
            
        def lose():
            global finalScore
            win.blit(blackScreen_1, (0, 0))
            loseText = font_1.render("YOU LOSE!", 1, (255, 255, 255))
            win.blit(loseText, (225, 275))
            loseText2 = font_14.render("You couldn't save the koala on time!", 1, (255, 255, 255))
            win.blit(loseText2, (75, 340))
            pygame.draw.rect(win, (255,100,10), pygame.Rect(125, 625, 200, 75)) #original 275
            winText3 = font_14.render("Quit", 1, (0, 0, 0))
            win.blit(winText3, (180, 635)) #original 330
            winText4 = font_14.render("Your score: 100", 1, (255, 255, 255))
            win.blit(winText4, (230, 400))
            pygame.draw.rect(win, (255,100,10), pygame.Rect(375, 625, 200, 75))
            winText5 = font6.render("Next Game", 1, (0, 0, 0))
            win.blit(winText5, (390, 640))
        opaci = 255
        run_1 = True
        while run_1:
            while gamePlaying_1 == False:
                win.fill((0, 0, 0))
                win.blit(bg_1, (0, 0))
                koalazzz.draw()
                for i in fires:
                    i.drawz()
                win.blit(blackScreen_1, (0, 0))
                pygame.draw.rect(win, (255,100,10), pygame.Rect(275, 625, 200, 75))
                text = font_14.render("Play Game", 1, (0, 0, 0))
                win.blit(text, (285, 635))
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        koalaGameOn = False
                        pygame.quit()
                    if (event.type == pygame.MOUSEBUTTONDOWN):
                        if pygame.mouse.get_pos()[0] in range(275, 475) and pygame.mouse.get_pos()[1] in range(625, 700):
                            startingPoint = pygame.time.get_ticks()
                            gamePlaying_1 = True
                pygame.display.update()
                    
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    koalaGameOn = False
                    run_1 = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    pos = pygame.mouse.get_pos()
                    for f in fires:
                        if f.hitbox[1] + f.hitbox[3] > pos[1] > f.hitbox[1]:
                            if f.hitbox[0] < pos[0] < f.hitbox[0] + f.hitbox[2]:
                                score_1 -= 25
                                f.hit()
                                fires.pop(fires.index(f))
                                break
                    if (won_1 or lost_1):
                        if pos[0] in range(125, 325) and pos[1] in range(625, 700):
                            koalaGameOn = False
                            run_1 = False
                        elif pos[0] in range(375, 575) and pos[1] in range(625, 700):
                            koalaGameOn = False
                            treeGameOn = True
                            run_1 = False
                            #pygame.quit()
                            
            win.blit(bg_1, (0, 0))
            koalazzz.draw()
            for i in fires:
                i.drawz()
        
            seconds = (pygame.time.get_ticks() - startingPoint) / 1000
            if (won_1 == False and lost_1 == False):
                time = 30 - int((seconds)) 
                score_1 -= time * 0.01
            countdown = font_13.render("Time left: " + str(time), 1, (255, 255, 255))
            win.blit(countdown, (300, 600))
            comment = font_13.render("Click on the fire to save the koala!", 1, (255, 255, 255))
            win.blit(comment, (200, 650))
            
            if koalazzz.rect.collidelist(fires) < 1:
                won_1 = True
                lost_1 = False
            else:
                won_1 = False
                
            if won_1 == False and time <= 0:
                lost_1 = True
                won_1 = False
            else:
                lost_1 = False
                
            if won_1:
                winz()
            elif lost_1:
                lose()
                
            if lost_1:
                score_1 = 100
                
            pygame.display.update()
        finalScore += score_1
    
    k = random.randint(1, 2)
    if k == 1:
        koalaGame()
    else:
        treeGame()    
    
    gameRunning = True
    while gameRunning == True:
        if (koalaGameOn):
            koalaGame()
        elif (treeGameOn):
            treeGame()
        else:
            gameRunning = False
    
    print(finalScore)
    scoreadder(finalScore)
    pygame.quit()                  


for frame in (menupage,playmenu,helpcause,leaderboard,cor,ear,fan):
    frame.grid(row=0,column=0,sticky="news")


#the widgets for menupage
im1 = Image.open(r"C:\Users\Home PC\Desktop\CS\future apple\PLAY.png")
f1= ImageTk.PhotoImage(im1)
im2 = Image.open(r"C:\Users\Home PC\Desktop\CS\future apple\home.jpeg")
f2= ImageTk.PhotoImage(im2)
im3 = Image.open(r"C:\Users\Home PC\Desktop\CS\future apple\leader.png")
f3= ImageTk.PhotoImage(im3)
im4 = Image.open(r"C:\Users\Home PC\Desktop\CS\future apple\cause.png")
f4= ImageTk.PhotoImage(im4)
im5 = Image.open(r"C:\Users\Home PC\Desktop\CS\future apple\settings.png")
f5= ImageTk.PhotoImage(im5)
label1=tkinter.Label(menupage,text="score",image=f2,borderwidth=0)
label1.pack(side="top")
button1=tkinter.Button(menupage, image=f1, command=lambda:raise_frame(playmenu),borderwidth=0 )
button2=tkinter.Button(menupage, image=f3, command=lambda:raise_frame(leaderboard),borderwidth=0)
button3=tkinter.Button(menupage, image=f4, command=lambda:raise_frame(helpcause),borderwidth=0)
button4=tkinter.Button(menupage, image=f5,borderwidth=0,command=lambda:raise_frame(fan))
button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")
button4.pack(side="top")
#playmenu
im6 = Image.open(r"C:\Users\Home PC\Desktop\CS\future apple\coronapic.png")
f6= ImageTk.PhotoImage(im6)
im7 = Image.open(r"C:\Users\Home PC\Desktop\CS\future apple\covid.png")
f7= ImageTk.PhotoImage(im7)
im8 = Image.open(r"C:\Users\Home PC\Desktop\CS\future apple\savearth.png")
f8= ImageTk.PhotoImage(im8)
im9 = Image.open(r"C:\Users\Home PC\Desktop\CS\future apple\earth.png")
f9= ImageTk.PhotoImage(im9)
im10 = Image.open(r"C:\Users\Home PC\Desktop\CS\future apple\back.png")
f10= ImageTk.PhotoImage(im10)
label2=tkinter.Label(playmenu,text="score",image=f6)
label2.pack(side="top")
button5=tkinter.Button(playmenu, image=f7,command=lambda:raise_frame(cor),borderwidth=0)
button5.pack(side="top")
label3=tkinter.Label(playmenu,text="score",image=f8)
label3.pack(side="top")
button6=tkinter.Button(playmenu, image=f9,command=lambda:raise_frame(ear),borderwidth=0)
button6.pack(side="top")
button7=tkinter.Button(playmenu, image=f10, command=lambda:raise_frame(menupage),borderwidth=0)
button7.pack()

#leaderboard
label4=tkinter.Label(leaderboard,text="LEADERBOARD",bg="#1fe046")
label4.pack()
label4.config(font=("Obilix Pro",20),fg="red")
label10=tkinter.Label(leaderboard,text=" Covid19 event",bg="#1fe046")
label10.config(font=("New Times Roman",20,),fg="blue")
label10.pack()                  
label5=tkinter.Label(leaderboard,text=str(s),bg="#1fe046")
label5.config(font=("New times Roman",10,),fg="black")                     
label5.pack()
label11=tkinter.Label(leaderboard,text=" Save the earth event",bg="#1fe046")
label11.config(font=("New Times Roman",20,),fg="green")
label11.pack()
label12=tkinter.Label(leaderboard,text=str(s2),bg="#1fe046")
label12.pack()
label12.config(font=("New times Roman",10,),fg="black")
button7=tkinter.Button(leaderboard, image=f10, command=lambda:raise_frame(menupage),borderwidth=0)
button7.pack()

#help the cause
label6=tkinter.Label(helpcause,text="THIS MONTH'S CAMPAIGN",bg="#1fe046")
label6.config(font=("New Times Roman",30),)
label6.pack()
label7=tkinter.Label(helpcause,text="COVID-19",bg="#1fe046",fg="Red")
label7.config(font=("New Times Roman",30))
label7.pack()
label8=tkinter.Label(helpcause,text="SPONSOR->",bg="#1fe046",fg="Red")
label8.config(font=("New Times Roman",30))
label8.pack()
label21=tkinter.Label(helpcause,text="Sponsor hyperlink and image here")
label21.config(font=("New Times Roman",20),bg="#1fe046",fg="blue")
label21.pack()
label18=tkinter.Label(helpcause,text="All scores will be coverted to a monetary amount\n which will be donated to COVID-19 hospitals",bg="#1fe046",fg="green")
label18.config(font=("New Times Roman",20))
label18.pack()
label13=tkinter.Label(helpcause,text="Money raised for Covid19 charity")
label13.config(font=("New Times Roman",20),bg="#1fe046")
label13.pack()
label14=tkinter.Label(helpcause,text=str(c))
label14.config(font=("New Times Roman",20),bg="#1fe046")
label14.pack()
label15=tkinter.Label(helpcause,text="Money raised for Save Earth charity")
label15.config(font=("New Times Roman",20),bg="#1fe046")
label15.pack()
label16=tkinter.Label(helpcause,text=str(d))
label16.config(font=("New Times Roman",20),bg="#1fe046")
label16.pack()
label17=tkinter.Label(helpcause,text="More about charities sponsored this month:")
label17.config(font=("New Times Roman",20),bg="#1fe046")
label17.pack()
label19=tkinter.Label(helpcause,text="charity no.1 hyperlink and image here")
label19.config(font=("New Times Roman",20),bg="#1fe046",fg="blue")
label19.pack()
label20=tkinter.Label(helpcause,text="charity no.2 hyperlink and image here")
label20.config(font=("New Times Roman",20),bg="#1fe046",fg="blue")
label20.pack()
button7=tkinter.Button(helpcause, image=f10, command=lambda:raise_frame(menupage),borderwidth=0)
button7.pack(side="bottom")
#cor
label9=tkinter.Label(cor,text="There are simple yet very powerful tools,\nwhich can help us fight the pandemic\nsocial distancing and washing hands are some of them.\nWith the following games\nwe hope you learn how to be safe\n in the pandemic.\n good luck!",bg="#1fe046")
label9.config(font=("New Times Roman",20))
label9.pack()
button8=tkinter.Button(cor, image=f1,borderwidth=0,command=asmaan)
button8.pack()
button7=tkinter.Button(cor, image=f10, command=lambda:raise_frame(playmenu),borderwidth=0,)
button7.pack()
#ear
label13=tkinter.Label(ear,text="There are many crises ailing our planet,\nwhich are not being informed about enough.\nWith this game we hope to spread awareness about them,\nSo you are more vigilant and do your part in any way possible.\n good luck!",bg="#1fe046")
label13.config(font=("New Times Roman",20))
label13.pack()
button8=tkinter.Button(ear, image=f1,borderwidth=0,command=zameen)
button8.pack()
button7=tkinter.Button(ear, image=f10, command=lambda:raise_frame(playmenu),borderwidth=0)
button7.pack()
#fan
label31=tkinter.Label(fan,text="Enter Username",bg="#1fe046")
label31.config(font=("New Times Roman",20))
button7=tkinter.Button(fan, image=f10, command=lambda:raise_frame(playmenu),borderwidth=0)
button50=tkinter.Button(fan, image=f1,command=bleh1,borderwidth=0 )
enterbox=tkinter.Entry(fan)
label31.pack()
enterbox.pack()
button7.pack()

raise_frame(menupage)
window.mainloop()

