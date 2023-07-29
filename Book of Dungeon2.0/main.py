# Imports
import sys
import pygame
import functions

# Configuration
pygame.init()
pygame.display.set_caption("Book of Dungeon")

caption_logo = pygame.image.load("image\guitar\caption_logo.png")
pygame.display.set_icon(caption_logo)

width, height = 1618, 1000
screen = pygame.display.set_mode((width, height))

#색깔
Black = (12,12,12)
White = (255,255,255)
Red = (233,100,100)
Green = (60,179,113)
Blue = (74,168,216)
Gray = (211,211,211)
Background = (246,246,246)
BBakground = (20, 20, 20)

def screen_update():
    pygame.display.update()

#폰트 가져오기
font = pygame.font.SysFont("airal",30)


#이미지 로드 클래스
class ScreenObject:
    def __init__(self,sort,content,pos_x=404.5,pos_y=250,blanding = True,txt_color = Black,font_value = ["airal",50]):
        self.sort = sort
        self.content = content
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.txt_color = txt_color
        self.blanding = blanding
        self.font = pygame.font.SysFont(font_value[0],font_value[1])
        
        if sort == "img":
            self.img= pygame.image.load(content)
            self.rect = self.img.get_rect()
            self.rect.centerx = pos_x
            self.rect.centery = pos_y
        
        elif sort == "txt":
            self.txt = self.font.render(content,blanding,txt_color)
            self.rect = self.txt.get_rect()
            self.rect.centerx = pos_x
            self.rect.centery = pos_y
    
    def rebuild(self):
        if self.sort == "img":
            self.img= pygame.image.load(self.content)
            self.rect = self.img.get_rect()
            self.rect.centerx = self.pos_x
            self.rect.centery = self.pos_y
        
        elif self.sort == "txt":
            self.txt = self.font.render(self.content,self.blanding,self.txt_color)
            self.rect = self.txt.get_rect()
            self.rect.centerx = self.pos_x
            self.rect.centery = self.pos_y

functions.intro()

# Configuration
pygame.init()
pygame.display.set_caption("Book of Dungeon")

caption_logo = pygame.image.load("image\guitar\caption_logo.png")
pygame.display.set_icon(caption_logo)

width, height = 1618, 1000
screen = pygame.display.set_mode((width, height))

Background = (246,246,246)

#폰트 가져오기
font = pygame.font.SysFont("airal",30)

###################
#function 가져오기#
###################

screen_update = functions.screen_update
class_Stage = functions.Stage
fadeout = functions.fadeout

font = pygame.font.SysFont('airal', 50)

objects = []

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False,img = "image/UI/button01.png",img_blank = "image/UI/button01_blank.png"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.img = ScreenObject("img",img,pos_x=x+width/2,pos_y=y+height/2)
        self.img_blank = ScreenObject("img",img_blank,pos_x=x+width/2,pos_y=y+height/2)
        self.txt = ScreenObject("txt",buttonText,pos_x=x+width/2,pos_y=y+height/2)
        self.surface = pygame

        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        screen.blit(self.img.img,self.img.rect)

        if self.img.rect.collidepoint(mousePos):

            screen.blit(self.img_blank.img,self.img_blank.rect)
            if pygame.mouse.get_pressed(num_buttons=3)[0]:

                screen.blit(self.img_blank.img,self.img_blank.rect)
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        screen.blit(self.txt.txt,self.txt.rect)

def myFunction1():
    tro_bgm = functions.tro_bgm
    tro_bgm.fadeout(2000)
    txt0 = functions.ScreenObject("txt","Loading...",pos_x=809,pos_y=500,txt_color=Background)
    screen_update()
    screen.blit(txt0.txt,txt0.rect)
    fadeout(color = (20, 20, 20))

    First_Stage = class_Stage()

    First_Stage.init()


def myFunction2():
    global manual_window
    manual_window = True   

def myFunction3():
    pygame.quit()
    sys.exit()


Button(120, 800, 400, 100, 'game start', myFunction1)
Button(620, 800, 400, 100, 'game menual', myFunction2)
Button(1120, 800, 400, 100, 'exit', myFunction3)

global manual_window
manual_window = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:                   
            manual_window = False

    if manual_window:
        image1 = pygame.image.load(r"image\manual\manual .png")
        screen.blit(image1, (0, 0))
        Explanation_txt3 = ScreenObject("txt","Press Any Key",txt_color=(0,0,0),pos_x=809,pos_y=900)
        screen.blit(Explanation_txt3.txt,Explanation_txt3.rect)
    
    else:
        screen.fill((20, 20, 20))
        main_screen_background = functions.ScreenObject("img",r"image\background\main screen background.jpg",pos_x = 809,pos_y=500)
        screen.blit(main_screen_background.img,main_screen_background.rect)
        for object in objects:
            object.process()

    pygame.display.flip()
                