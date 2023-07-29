import pygame
import random
import time
import sys
import os
import webbrowser
import datetime

os.getcwd()
fpsClock=pygame.time.Clock()
###########
#기본 세팅#
###########

#색깔
Black = (12,12,12)
White = (255,255,255)
Red = (233,100,100)
Green = (60,179,113)
Blue = (74,168,216)
Gray = (128,128,128)
Background = (246,246,246)
BBakground = (20, 20, 20)
Legend_skill_txt_color = (127,255,212)
Epic_skill_txt_color = (212,175,55)
Normal_skill_txt_color = (162,162,162)


pygame.init()
pygame.font.init()

size = [1618,1000]

screen = pygame.display.set_mode(size)

screen.fill(Background)

#폰트 가져오기
font = pygame.font.SysFont("airal",50)

################
#필수 함수 모음#
################

#화면 업데이트
def screen_update():
    pygame.display.update()

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

#텍스트 창 클래스
class ScreenTxt:
    def __init__(self,sort = 1,name = "I",txt1_1_content ="Shall I compare thee to a summer's day?" ,txt2_1_content="Shall I compare thee to a summer's day?",txt2_2_content="Shall I compare thee to a summer's day?"):
        self.sort = sort
        self.txt1_1_content = txt1_1_content
        self.txt2_1_content = txt2_1_content
        self.txt2_2_content = txt2_2_content
        self.name = name

        txt0_name = ScreenObject("txt",name,pos_x=215,pos_y=575,txt_color=White) 
        txt1_1 = ScreenObject("txt",txt1_1_content,pos_x=759,pos_y=750,txt_color=White)
        txt2_1 = ScreenObject("txt",txt2_1_content,pos_x=759,pos_y=700,txt_color=White)
        txt2_2 = ScreenObject("txt",txt2_2_content,pos_x=759,pos_y=800,txt_color=White)       
        
        pygame.draw.rect(screen,Gray,(50,550,1518,400))
        pygame.draw.rect(screen,Background,(50,550,1518,400),5)
        pygame.draw.rect(screen,Gray,(65,535,300,80))
        pygame.draw.rect(screen,Background,(65,535,300,80),5)
        
        screen.blit(txt0_name.txt,txt0_name.rect)
        
        if sort == 1:
            screen.blit(txt1_1.txt,txt1_1.rect)
        
        elif sort == 2:
            screen.blit(txt2_1.txt,txt2_1.rect)
            screen.blit(txt2_2.txt,txt2_2.rect)

        screen_update()

#페이드아웃 
def fadeout(width = 1618, height = 1000 ,loop = 120,color = Background): 
    fade = pygame.Surface((width, height))
    fade.fill(color)
    for alpha in range(0, loop):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(10)

#기타 객체
jeonjugo_logo = ScreenObject("img",content="image\guitar\jeonjugo_logo.png",pos_x=809,pos_y=500)

pygame.mixer.init() 
map_bgm00 = pygame.mixer.Sound("bgm\map\eight_bit (online-audio-converter.com).wav")
#tro_bgm = pygame.mixer.music.load("bgm/main_lobby/AdhesiveWombat - Night Shade.mp3")
tro_bgm = pygame.mixer.Sound("bgm\main_lobby\AdhesiveWombat - Night Shade (online-audio-converter.com).wav")

tro_bgm.set_volume(0.1)

map_bgm00.set_volume(0.1)

intro_img01 = ScreenObject("img","image/intro/1.png",pos_x=809,pos_y=500)
intro_img02 = ScreenObject("img","image/intro/2.png",pos_x=809,pos_y=500)
intro_img03 = ScreenObject("img","image/intro/3.png",pos_x=809,pos_y=500)
intro_img04 = ScreenObject("img","image/intro/4.png",pos_x=809,pos_y=500)
intro_img05 = ScreenObject("img","image/intro/5.png",pos_x=809,pos_y=500)
intro_img06 = ScreenObject("img","image/intro/6.png",pos_x=809,pos_y=500)
intro_img07 = ScreenObject("img","image/intro/7.png",pos_x=809,pos_y=500)
intro_img08 = ScreenObject("img","image/intro/8.png",pos_x=809,pos_y=500)
intro_img09 = ScreenObject("img","image/intro/9.png",pos_x=809,pos_y=500)
intro_img010 = ScreenObject("img","image/intro/10.png",pos_x=809,pos_y=500)

fight_screen_background = ScreenObject("img","image/background/fight_screen_background.png",pos_x=809,pos_y=500)

stage_skill_bar = ScreenObject("img","image/UI/stage_skill_bar.png",pos_x=809,pos_y=500)

#인트로
def intro():
    screen.fill(Background)
    screen.blit(jeonjugo_logo.img,jeonjugo_logo.rect)

    screen_update()
    tro_bgm.play(-1)
    time.sleep(1)
    fadeout(loop = 50,color=Black)

    screen.blit(intro_img01.img,intro_img01.rect)
    screen_update()
    time.sleep(2.3)
    fadeout(color=Black)
    
    screen.blit(intro_img02.img,intro_img02.rect)
    screen_update()
    time.sleep(1)
    fadeout(color=Black,loop = 50)
    
    screen.blit(intro_img03.img,intro_img03.rect)
    screen_update()
    time.sleep(0.4)
    
    screen.blit(intro_img04.img,intro_img04.rect)
    screen_update()
    time.sleep(0.4)
    
    screen.blit(intro_img05.img,intro_img05.rect)
    screen_update()
    time.sleep(0.4)
    fadeout(loop = 50,color=Black)

    screen.blit(intro_img06.img,intro_img06.rect)
    screen_update()
    time.sleep(2.5)
    fadeout(loop = 50,color=Black)

    screen.blit(intro_img07.img,intro_img07.rect)
    screen_update()
    time.sleep(1)
    fadeout(loop = 50,color=Black)

    screen.blit(intro_img08.img,intro_img08.rect)
    screen_update()
    time.sleep(0.5)


    screen.blit(intro_img09.img,intro_img09.rect)
    screen_update()
    time.sleep(0.5)


    screen.blit(intro_img010.img,intro_img010.rect)
    screen_update()
    time.sleep(0.5)
    fadeout(loop = 100,color=(1,127,124))


################
#스테이지 클래스#
################# 
map_size = [[],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
]

# [img,type]
enemy_value_list = [["image/character/enemy_fire.png","fire","image\character\enemy_fire_set.png"],["image/character/enemy_grass.png","dendro","image\character\enemy_grass_set.png"],["image/character/enemy_water.png","water","image\character\enemy_water_set.png"]]

#tile list
tile_list = ["image/UI/tile01.jpg"]

class Skill:
    def __init__(self,name = None,sort = "attack",type = "fire",value01 = 20,value02 = 30,img = None,txt = "Test",name_color = Normal_skill_txt_color):
        self.name = name
        self.sort = sort
        self.type = type
        self.value01 = value01
        self.value02 = value02
        self.img = ScreenObject(sort = "img", content= img)
        self.txt = txt
        self.name_color = name_color

        if type== None:
            self.enemy_strong_type=None
            self.enemy_weak_type=None
        
        elif type=="fire":
            self.enemy_strong_type="dendro"
            self.enemy_weak_type="water"

        elif type=="water":
            self.enemy_strong_type="fire"
            self.enemy_weak_type="dendro"

        elif type=="dendro":
            self.enemy_strong_type="water"
            self.enemy_weak_type="fire"

normal_attack = Skill(name = "normal_attack",type= None , img="image/UI/skill/normal_attack.gif",txt="actually muscle wizard",value01=5,value02=10,name_color=Normal_skill_txt_color)   

blooming = Skill(name = "blooming",type= "dendro" , img="image/UI/skill/blooming.gif",txt="sprouting to the sky",value01=15,value02=25,name_color=Epic_skill_txt_color)
healing = Skill(name = "healing",type= "dendro" , img="image/UI/skill/healing.gif",txt="maybe it will not heal you but..",value01=10,value02=15,name_color=Normal_skill_txt_color)
leaf_blade = Skill(name = "leaf blade",type= "dendro" , img="image/UI/skill/leaf_blade.gif",txt="casuing grass irritation",value01=25,value02=30,name_color=Legend_skill_txt_color)

fire_arrow = Skill(name = "fire arrow",type= "fire" , img="image/UI/skill/fire_arrow.gif",txt="penetrating with flame",value01=15,value02=25,name_color=Normal_skill_txt_color)
hell_fire = Skill(name = "hell fire",type= "fire" , img="image/UI/skill/hell_fire.gif",txt="opening the hell gate",value01=10,value02=15,name_color=Normal_skill_txt_color)
explosion = Skill(name = "explosion",type= "fire" , img="image/UI/skill/explosion.gif",txt="i'm feeling like there's a egg",value01=25,value02=30,name_color=Legend_skill_txt_color)

tsunami = Skill(name = "tsunami",type= "water" , img="image/UI/skill/tsunami.gif",txt="overwhelming waves",value01=25,value02=30,name_color=Legend_skill_txt_color)
water_tornado = Skill(name = "water tornado",type= "water" , img="image/UI/skill/water_tornado.gif",txt="blowing away",value01=15,value02=25,name_color=Epic_skill_txt_color)
water_shot = Skill(name = "water shot",type= "water" , img="image/UI/skill/water_shot.png",txt="bubbles but big",value01=10,value02=15,name_color=Normal_skill_txt_color)

skill_list = [normal_attack,blooming,healing,leaf_blade,fire_arrow,hell_fire,explosion,tsunami,water_tornado,water_shot]

class Character:
    def __init__(self,name = "protago",skill01 = "none",skill02 = "none",pos_x = 0,pos_y = 0,img = "image\character\prota.png",img_set = "image\character\prota.png",hp = 100, type = None) -> None:
        self.name = name
        self.skill_01 = skill01
        self.skill_02 = skill02
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.img = img
        self.object = ScreenObject(sort="img",content=img)
        self.img_set = ScreenObject(sort="img",content=img_set,pos_x=809,pos_y=300)
        self.hp = hp
        self.type = type
 

    def __del__(self):
        print("deleted")

    def moving(self):
        #print(self.name,self.pos_x,self.pos_y) 
        self.object.pos_x = map_size[self.pos_x][self.pos_y].pos_x + 50
        self.object.pos_y = map_size[self.pos_x][self.pos_y].pos_y + 50
        
        self.object.rebuild()
        screen.blit(self.object.img,self.object.rect)
        screen_update()


class StageSet:
    def __init__(self,mode = "none",size_x = 8,size_y = 10,background = "none",skill01 = None,skill02 = None) -> None:
        
        self.map_size = map_size
        self.tile_img = ScreenObject("img",content = random.choice(tile_list))
        self.mode = mode
        self.size_x = size_x
        self.size_y = size_y
        self.bakground = background
        self.skill01 = skill01
        self.skill02 = skill02

        class MapBlock:
            def __init__(self01,self,name,):
                self01.name = name
                self01.mode = self.mode
                self01.pos_x = name[0]
                self01.pos_y = name[1]
                self01.prese = False

            def build(self01):
                self01.prese = False
                self.tile_img.pos_x = self01.pos_x + 50
                self.tile_img.pos_y = self01.pos_y + 50

                self.tile_img.rebuild()

                screen.blit(self.tile_img.img,self.tile_img.rect)
                pygame.draw.rect(screen,Black,(self01.pos_x,self01.pos_y,100,100),5)

        for i in range(0, self.size_x):
            for j in range(0, size_y):
                self.map_size[i].append(MapBlock(self,name=[i,j]))
                
                self.map_size[i][j].pos_x = 500 + 100*j 

                self.map_size[i][j].pos_y = 100 + 100*i 
    
    def stage_rebuild(self):
        screen.blit(stage_skill_bar.img,stage_skill_bar.rect)

        self.skill01.img.pos_x = 240
        self.skill01.img.pos_y = 210
        self.skill01.img.rebuild()
        screen.blit(self.skill01.img.img,self.skill01.img.rect)

        self.skill02.img.pos_x = 240
        self.skill02.img.pos_y = 660
        self.skill02.img.rebuild()        
        screen.blit(self.skill02.img.img,self.skill02.img.rect)
        
        type_color = None

        if self.skill01.type == "dendro":
            type_color = Green
        
        elif self.skill01.type == "fire":
            type_color = Red
        
        elif self.skill01.type == "water":
            type_color = Blue
        
        else:
            type_color = Gray

        txt011 = ScreenObject("txt","{}".format(self.skill01.name),txt_color=type_color,pos_x = self.skill01.img.pos_x,pos_y=405)
        txt012 = ScreenObject("txt","{} ~ {}".format(self.skill01.value01,self.skill01.value02),pos_x = self.skill01.img.pos_x,pos_y=450,txt_color = self.skill01.name_color)
        
        if self.skill02.type == "dendro":
            type_color = Green
        
        elif self.skill02.type == "fire":
            type_color = Red
        
        elif self.skill02.type == "water":
            type_color = Blue
        
        else:
            type_color = Gray

        txt021 = ScreenObject("txt","{}".format(self.skill02.name),txt_color=type_color,pos_x = self.skill02.img.pos_x,pos_y=865)
        txt022 = ScreenObject("txt","{} ~ {}".format(self.skill02.value01,self.skill02.value02),pos_x = self.skill02.img.pos_x,pos_y=910,txt_color = self.skill02.name_color)

        screen.blit(txt011.txt,txt011.rect)
        screen.blit(txt012.txt,txt012.rect)
        screen.blit(txt021.txt,txt021.rect)
        screen.blit(txt022.txt,txt022.rect)


        

        for i in range(0,len(self.map_size)):
            for j in range(0,len(self.map_size[i])):
                self.map_size[i][j].build()



##########################    
class Stage:
    global objectss
    objectss = []
    def __init__(self,enemy_count = 5,stage_set_value = ["none",8,10,"none"]):    
        prota_attack_skill01 = random.choice(skill_list)
    
        while True:
            check = random.choice(skill_list)

            if check.name == prota_attack_skill01.name:
                
                continue
            else:
                prota_attack_skill02 = check
                break
 
        self.stage = 10
        self.prota = Character(skill01 = prota_attack_skill01,skill02=prota_attack_skill02)
        self.stage_set_value = stage_set_value
        self.stage_field = StageSet(mode = stage_set_value[0],size_x = stage_set_value[1],size_y = stage_set_value[2],background = stage_set_value[3],skill01=prota_attack_skill01,skill02=prota_attack_skill02)
        self.enemy_count = enemy_count
        self.enemy_list = []
                
        for i in range(1,enemy_count+1):
            enemy_value =  random.choice(enemy_value_list)
            self.enemy_list.append(Character(hp=50,name="enemy{}".format(i), img=enemy_value[0],type=enemy_value[1],img_set=enemy_value[2]))

            self.enemy_list[i-1].pos_x = random.randint(0,stage_set_value[1]-1)
            self.enemy_list[i-1].pos_y = random.randint(0,stage_set_value[2]-1)

        
    def fight(self):
        check = False
        enemy_list_number = None

        

        for k in range(0,len(self.enemy_list)):
            if (self.enemy_list[k].pos_x == self.prota.pos_x and self.enemy_list[k].pos_y == self.prota.pos_y):
                enemy_list_number = k 
                check =False
                fadeout(color=Background)
                screen_update()

                End = False

                while not End:
########################################################################################################################
                    pygame.init()
                    width, height = 1618, 1000
                    screen = pygame.display.set_mode((width, height))

                    font = pygame.font.SysFont('airal', 50)

                    objects = []

                    global Explanation
                    Explanation = False

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

                    def calcuate(min,max,enemy_hp,enemy_type,a,b):
                        ch=random.randint(0,1)
                        prota_damage=random.randint(min,max)
                        if ch==0:
                            ch1=random.randint(0,2)

                            if ch1==0:
                                if a==enemy_type:
                                    damage_txt1="You attacked the enemy with a strong attribute. damage:"+str(prota_damage*2)
                                    self.enemy_list[k].hp=enemy_hp-prota_damage*2
                                elif b==enemy_type:
                                    if prota_damage-10 <= 0:
                                        damage_txt1="You attacked the enemy with a weak attribute. damage:"+str(0)
                                        self.enemy_list[k].hp=enemy_hp
                                    else:
                                        damage_txt1="You attacked the enemy with a weak attribute. damage:"+str(prota_damage-10)
                                        self.enemy_list[k].hp=enemy_hp-(prota_damage-10)
                                else:
                                    damage_txt1="You attacked the enemy with normal attributes. damage:"+str(prota_damage)
                                    self.enemy_list[k].hp=enemy_hp-prota_damage

                                enemy_damage=random.randint(10,20)
                                damage_txt2="enemy attacked you. damage:"+str(enemy_damage)
                                self.prota.hp=self.prota.hp-enemy_damage

                            elif ch1==1:
                                if a==enemy_type:
                                    damage_txt1="You attacked the enemy with a strong attribute. damage:"+str(prota_damage*2)
                                    damage_txt1=str(prota_damage*2)
                                    self.enemy_list[k].hp=enemy_hp-prota_damage*2
                                elif b==enemy_type:
                                    damage_txt1=str(prota_damage-10)
                                    if prota_damage-10 <= 0:
                                        damage_txt1="You attacked the enemy with a weak attribute. damage:"+str(0)
                                        self.enemy_list[k].hp=enemy_hp
                                    else:
                                        damage_txt1="You attacked the enemy with a weak attribute. damage:"+str(prota_damage-10)
                                        self.enemy_list[k].hp=enemy_hp-(prota_damage-10)
                                else:
                                    damage_txt1="You attacked the enemy with normal attributes. damage:"+str(prota_damage)
                                    self.enemy_list[k].hp=enemy_hp-prota_damage
                                damage_txt2="dodged an enemy attack"

                            else:
                                damage_txt1="dodge your attack"
                                enemy_damage=random.randint(10,20)
                                damage_txt2="enemy attacked you. damage:"+str(enemy_damage)
                                self.prota.hp=self.prota.hp-enemy_damage

                        elif ch==1:
                            damage_txt1="the enemy defended"
                            defense=random.randint(10,20)
                            if a==enemy_type:
                                if prota_damage*2-defense <= 0:
                                    damage_txt2="You attacked the enemy with a strong attribute. damage:"+str(0)
                                    self.enemy_list[k].hp=enemy_hp
                                else:
                                    damage_txt2="You attacked the enemy with a strong attribute. damage:"+str(prota_damage*2-defense)
                                    self.enemy_list[k].hp=enemy_hp-(prota_damage*2-defense)
                            elif b==enemy_type:
                                if prota_damage-10-defense <= 0:
                                    damage_txt2="You attacked the enemy with a weak attribute. damage:"+str(0)
                                    self.enemy_list[k].hp=enemy_hp
                                else:
                                    damage_txt2="You attacked the enemy with a weak attribute. damage:"+str(prota_damage-10-defense)
                                    self.enemy_list[k].hp=enemy_hp-(prota_damage-10-defense)
                            else:
                                if prota_damage-defense <= 0:
                                    damage_txt2="You attacked the enemy with a normal attribute. damage:"+str(0)
                                    self.enemy_list[k].hp=enemy_hp
                                else:
                                    damage_txt2="You attacked the enemy with a normal attribute. damage:"+str(prota_damage-defense)
                                    self.enemy_list[k].hp=enemy_hp-(prota_damage-defense)

                        global Explanation1
                        Explanation1=damage_txt1
                        global Explanation2
                        Explanation2=damage_txt2

                        return None
                    
                    def skill1():
                        min=self.prota.skill_01.value01
                        max=self.prota.skill_01.value02
                        enemy_hp=self.enemy_list[k].hp
                        enemy_type=self.enemy_list[k].type
                        a=self.prota.skill_01.enemy_strong_type
                        b=self.prota.skill_01.enemy_weak_type
                        calcuate(min,max,enemy_hp,enemy_type,a,b)
                        global Explanation
                        Explanation = True
                    
                    def skill2():
                        min=self.prota.skill_02.value01
                        max=self.prota.skill_02.value02
                        enemy_hp=self.enemy_list[k].hp
                        enemy_type=self.enemy_list[k].type
                        a=self.prota.skill_02.enemy_strong_type
                        b=self.prota.skill_02.enemy_weak_type
                        calcuate(min,max,enemy_hp,enemy_type,a,b)
                        global Explanation
                        Explanation = True
                    
                    def fire_defense():
                        defense_Possibility=random.randint(0,1)
                        global damage_txt1
                        global damage_txt2

                        if defense_Possibility==1:
                            self.enemy_list[k].hp=self.enemy_list[k].hp-40
                            damage_txt1="you succeeded in counterattacking."
                            damage_txt2="the damage you inflicted damage:"+str(40)
                        else:
                            enemy_damage=random.randint(10,20)
                            self.prota.hp=self.prota.hp-enemy_damage
                            damage_txt1="you failed to fight back."
                            damage_txt2="damage done to you damage:"+str(enemy_damage)
                        
                        global Explanation1
                        Explanation1=damage_txt1
                        global Explanation2
                        Explanation2=damage_txt2

                        global Explanation
                        Explanation = True
                    
                    def water_defense():
                        defense_Possibility=random.randint(0,1)
                        global damage_txt1
                        global damage_txt2

                        if defense_Possibility==1:
                            self.prota.hp=self.prota.hp+20
                            damage_txt1="you succeeded in rearranging"
                            damage_txt2="HP cured cured:"+str(20)
                        else:
                            enemy_damage=random.randint(10,20)
                            damage_txt1="you failed to reorganize"
                            damage_txt2="damage done to you damage:"+str(enemy_damage)
                            self.prota.hp=self.prota.hp-enemy_damage
                        
                        global Explanation1
                        Explanation1=damage_txt1
                        global Explanation2
                        Explanation2=damage_txt2

                        global Explanation
                        Explanation = True
                    
                    def dendro_defense():
                        defense_Possibility=random.randint(0,4)
                        global damage_txt1
                        global damage_txt2

                        if defense_Possibility>=1:
                            damage_txt1="You have succeeded in a sneak attack"
                            damage_txt2="the damage you inflicted damage:"+str(10)
                            self.enemy_list[k].hp=self.enemy_list[k].hp-10
                        else:
                            enemy_damage=random.randint(10,20)
                            damage_txt1="You failed the sneak attack"
                            damage_txt2="damage done to you damage:"+str(enemy_damage)
                            self.prota.hp=self.prota.hp-enemy_damage
                        
                        global Explanation1
                        Explanation1=damage_txt1
                        global Explanation2
                        Explanation2=damage_txt2
                        
                        global Explanation
                        Explanation = True

                    Button(170, 800, 350, 100, self.prota.skill_01.name, skill1)
                    Button(640, 740, 150, 100, 'fire', fire_defense,img="image/UI/button02.png",img_blank="image/UI/button02_blank.png")
                    Button(720, 850, 150, 100, 'water', water_defense,img="image/UI/button02.png",img_blank="image/UI/button02_blank.png")
                    Button(800, 740, 150, 100, 'dendro', dendro_defense,img="image/UI/button02.png",img_blank="image/UI/button02_blank.png")
                    Button(1070, 800, 350, 100, self.prota.skill_02.name, skill2)

                    screen.fill(BBakground)
                    screen_update()

                    while self.enemy_list[k].hp > 0 and self.prota.hp > 0 :
                        if self.prota.hp <= 0:
                            print("You died")
                            pygame.quit()
                            sys.exit()
                        for event in pygame.event.get():
                            
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            if event.type == pygame.KEYDOWN:                   
                                Explanation = False

                        screen.blit(fight_screen_background.img,fight_screen_background.rect)
                        screen.blit(self.enemy_list[k].img_set.img,self.enemy_list[k].img_set.rect)

                        if Explanation:
                            pygame.draw.rect(screen, Gray, (100, 680, 1400, 300))
                            pygame.draw.rect(screen, Background, (100, 680, 1400, 300),5)

                            Explanation_txt1 = ScreenObject("txt",Explanation1,pos_x=795,pos_y=710,txt_color=(255,255,255))
                            screen.blit(Explanation_txt1.txt,Explanation_txt1.rect)

                            Explanation_txt2 = ScreenObject("txt",Explanation2,pos_x=795,pos_y=760,txt_color=(255,255,255))
                            screen.blit(Explanation_txt2.txt,Explanation_txt2.rect)

                            Explanation_txt3 = ScreenObject("txt","Press Any Key",txt_color=Background,pos_x=809,pos_y=900)
                            screen.blit(Explanation_txt3.txt,Explanation_txt3.rect)

                        else:
                            pygame.draw.rect(screen, Gray, (100, 680, 1400, 300))
                            pygame.draw.rect(screen, Background, (100, 680, 1400, 300),5)
                            pygame.draw.rect(screen, (255,0,0), (635, 735, 160, 110),5)
                            pygame.draw.rect(screen, (0,0,255), (715, 845, 160, 110),5)
                            pygame.draw.rect(screen, (0,255,0), (795, 735, 160, 110),5)

                            for object in objects:
                                object.process()

                            def_type_txt = ScreenObject("txt","-defense type-",pos_x=795,pos_y=710,txt_color=Black)
                            screen.blit(def_type_txt.txt,def_type_txt.rect)
                        
                        hp1 = ScreenObject("txt","{}".format((self.enemy_list[k].hp)),pos_x=809,pos_y=100,font_value=["airal",150],txt_color=(217,33,33))
                        screen.blit(hp1.txt,hp1.rect)
                        hp2 = ScreenObject("txt","My Hp:{}".format((self.prota.hp)),pos_x=300,pos_y=640,font_value=["airal",100],txt_color=(217,33,33))
                        screen.blit(hp2.txt,hp2.rect)

                        pygame.display.flip()

                    if self.enemy_list[k].hp <= 0:
                        del self.enemy_list[enemy_list_number]
                        screen.blit(fight_screen_background.img,fight_screen_background.rect)
                        pygame.draw.rect(screen, Gray, (100, 680, 1400, 300))
                        pygame.draw.rect(screen,Background, (100, 680, 1400, 300),5)

                        win = ScreenObject("txt","You defeated it!",pos_x=759,pos_y=770,font_value=["airal",100],txt_color=Black)
                        screen.blit(win.txt,win.rect)
                        screen_update()                
                        time_check = time.time()

                        while True:
                            
                            time_check_check = time.time()
                            print("test")
                            if time_check_check - time_check > 3:
                                End= True
                                break

                            for event in pygame.event.get():
                            
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()

                    elif self.prota.hp <= 0:      
                        map_bgm00.stop()  
                        End= True            
                        fadeout(1618,1000,color=BBakground)
                        ScreenTxt(1,"???","as expected")
                        
                        time_check = time.time()

                        while True:
                            time_check_check = time.time()
                            if time_check_check - time_check > 1:
                                break
                            for event in pygame.event.get():
                            
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()


                        time_check = time.time()

                        while True:
                            time_check_check = time.time()
                            if time_check_check - time_check > 2:
                                sys.exit()

                            for event in pygame.event.get():
                            
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                    End= True
                    check = True
##################################################################################################################
                break

        if check == True:
            #print(self.enemy_list[k])
            #print(self.enemy_list)
            print("test")
            screen_update()
            #del self.enemy_list[enemy_list_number]
            print(self.enemy_list)
            fadeout(color=BBakground)

            screen.fill(White)
            move_Background=ScreenObject("img",r"image\background\battle screen background.png",pos_x = 809,pos_y=500)
            screen.blit(move_Background.img,move_Background.rect)

            self.stage_field.stage_rebuild()
            
            self.prota.moving()
            for k in self.enemy_list:
                k.moving()
            screen_update()
        
        else:
            return None
    
    def ending_click(self):
                
        End = False
        while not End:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:                   
                    End = True
                    return None
            
                elif event.type == pygame.QUIT:
                    sys.exit()


    def ending(self):
        def ending_txt(content = None):
            ScreenTxt(name = "???",txt1_1_content=content)
            self.ending_click()
            fadeout(loop = 50,color=Black)
        
        map_bgm00.fadeout(3)
        fadeout(color=Black)
        time.sleep(1)

        ending_txt("Oh")
        ending_txt("Unexpected")
        ending_txt("Don't you wonder why you here?")
        ending_txt("\"Who take me here? and for what reason?\"")
        ending_txt("...")
        ending_txt("Before you find the answer")
        ending_txt("You must first get used to this world")
        ending_txt("We will come back when you get ready")


        self.outro()

    def outro(self):
        tro_bgm.play()
        time.sleep(1)
        
        outro_img01 = ScreenObject("img","image/outro/1.png",pos_x=809,pos_y=500)
        outro_img02 = ScreenObject("img","image/outro/2.png",pos_x=809,pos_y=500)
        outro_img03 = ScreenObject("img","image/outro/3.png",pos_x=809,pos_y=500)

        screen.blit(outro_img01.img,outro_img01.rect)
        screen_update()

        time.sleep(2)
        fadeout(loop=120,color=Black)
        
        screen.blit(outro_img02.img,outro_img02.rect)
        screen_update()

        time.sleep(2)
        fadeout(loop=120,color=Black)
        
        screen.blit(outro_img03.img,outro_img03.rect)
        screen_update()

        time.sleep(2)
        fadeout(loop=120,color=Black)

        End = False
        while not End:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def init(self):
        
        End = False
        
        type_color = None

        if self.prota.skill_01.type == "dendro":
            type_color = Green
        
        elif self.prota.skill_01.type == "fire":
            type_color = Red
        
        elif self.prota.skill_01.type == "water":
            type_color = Blue

        else:
            type_color = Gray

        txt11 = ScreenObject("txt","{} (type:{})".format(self.prota.skill_01.name,self.prota.skill_01.type),pos_x = self.prota.skill_01.img.pos_x,pos_y=500,txt_color = type_color)
        txt12 = ScreenObject("txt","Minimum:{}   Maximum:{}".format(self.prota.skill_01.value01,self.prota.skill_01.value02),pos_x = self.prota.skill_01.img.pos_x,pos_y=600,txt_color=self.prota.skill_01.name_color)
        txt13 = ScreenObject("txt","{}".format(self.prota.skill_01.txt),txt_color=Background,pos_x = self.prota.skill_01.img.pos_x,pos_y=700)

        self.prota.skill_02.img.pos_x = 1213.5
        self.prota.skill_02.img.rebuild()
        
        if self.prota.skill_02.type == "dendro":
            type_color = Green
        
        elif self.prota.skill_02.type == "fire":
            type_color = Red
        
        elif self.prota.skill_02.type == "water":
            type_color = Blue
        
        else:
            type_color = Gray

        txt21 = ScreenObject("txt","{} (type:{})".format(self.prota.skill_02.name,self.prota.skill_02.type),pos_x = self.prota.skill_02.img.pos_x,pos_y=500,txt_color = type_color)
        txt22 = ScreenObject("txt","Minimum:{}   Maximum:{}".format(self.prota.skill_02.value01,self.prota.skill_02.value02),pos_x = self.prota.skill_02.img.pos_x,pos_y=600,txt_color=self.prota.skill_02.name_color)
        txt23 = ScreenObject("txt","{}".format(self.prota.skill_02.txt),txt_color=Background,pos_x = self.prota.skill_02.img.pos_x,pos_y=700)

        txt00 = ScreenObject("txt","Press Any Key",txt_color=Background,pos_x=809,pos_y=900)
        
        screen.blit(self.prota.skill_01.img.img,self.prota.skill_01.img.rect)
        screen.blit(self.prota.skill_02.img.img,self.prota.skill_02.img.rect)
        screen.blit(txt11.txt,txt11.rect)
        screen.blit(txt12.txt,txt12.rect)
        screen.blit(txt13.txt,txt13.rect)
        screen.blit(txt21.txt,txt21.rect)
        screen.blit(txt22.txt,txt22.rect)
        screen.blit(txt23.txt,txt23.rect)
        screen.blit(txt00.txt,txt00.rect)
        
        ###############################
        global checkk
        checkk = False
        global checkk_time
        checkk_time = None
        objectss = []

        for k in [self.prota.skill_01,self.prota.skill_02]:
            if k.name == "explosion":
                ob = k
                objectss = []

                class Button_2():
                    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
                        
                        self.x = x
                        self.y = y
                        self.width = width
                        self.height = height
                        self.onclickFunction = onclickFunction
                        self.onePress = onePress
                        self.alreadyPressed = False

                        self.buttonSurface = pygame.Surface((self.width, self.height))
                        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

                        self.buttonSurf = font.render(buttonText, True, (8,8,8))
                        objectss.append(self)
                        
                    def process(self):
                        mousePos = pygame.mouse.get_pos()
                        self.buttonSurface.fill(Black)
                        if self.buttonRect.collidepoint(pygame.mouse.get_pos()):
                            self.buttonSurface.fill(BBakground)
                            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                                self.buttonSurface.fill(BBakground)
                                if self.onePress:
                                    self.onclickFunction()
                                elif not self.alreadyPressed:
                                    self.onclickFunction()
                                    self.alreadyPressed = True
                            else:
                                self.alreadyPressed = False

                        self.buttonSurface.blit(self.buttonSurf, [
                            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
                            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
                        ])
                        screen.blit(self.buttonSurface, self.buttonRect)

                def explosion():
                    global checkk
                    global checkk_time

                    checkk = True
                    
                    
                    webbrowser.open("https://www.youtube.com/watch?v=-8rTfTm6JN0")
                    fill_it = pygame.draw.rect(screen,BBakground,(ob.img.pos_x-250,ob.img.pos_y-150,809,1000))
                    checkk_time = time.time()
                    #color_list = [(255,0,0),(255,50,0),(255,255,0),(0,255,0),(0,0,255),(0,5,255),(100,0,255)]
                    for i in range(0,23+1):
                        a = random.randint(0,255)
                        b = random.randint(0,255)
                        c = random.randint(0,255)
                        txt333 = ScreenObject("txt","bakuretsu bakuretsu la la la",pos_x=ob.img.pos_x,pos_y=50 + i*40,txt_color=(a,b,c))
                        screen.blit(txt333.txt,txt333.rect)

                    screen_update()
                    

                Button_2(x=k.img.pos_x-150,y=k.img.pos_y-150,width=300,height=300,buttonText="easteregg :)",onclickFunction= explosion)
        
        screen_update()
  

        while not End:
            if checkk == True:
                ttime = time.time()

                if  ttime - checkk_time >= 0.1:
                    for i in range(0,23+1):
                        a = random.randint(0,255)
                        b = random.randint(0,255)
                        c = random.randint(0,255)
                        txt333 = ScreenObject("txt","bakuretsu bakuretsu la la la",pos_x=ob.img.pos_x,pos_y=50 + i*40,txt_color=(a,b,c))
                        screen.blit(txt333.txt,txt333.rect)
                        
                        
                        checkk_time = time.time()

                    screen_update()
                        
            for objectsss in objectss:
                objectsss.process()
            
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:                   
                    fadeout(color=Gray)
                    map_bgm00.play(-1)
                    End = True

                elif event.type == pygame.QUIT:
                    sys.exit()
                    
        screen.blit(self.prota.skill_01.img.img,self.prota.skill_01.img.rect)
        screen.blit(self.prota.skill_02.img.img,self.prota.skill_02.img.rect)
        screen.blit(txt11.txt,txt11.rect)
        screen.blit(txt12.txt,txt12.rect)
        screen.blit(txt13.txt,txt13.rect)
        screen.blit(txt21.txt,txt21.rect)
        screen.blit(txt22.txt,txt22.rect)
        screen.blit(txt23.txt,txt23.rect)
        screen.blit(txt00.txt,txt00.rect)

        screen_update()

        while not End:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:                   
                    fadeout(color=Gray)
                    map_bgm00.play(-1)
                    End = True
                
                elif event.type == pygame.QUIT:
                    sys.exit()
        
        move_Background=ScreenObject("img",r"image\background\battle screen background.png",pos_x = 809,pos_y=500)
        screen.blit(move_Background.img,move_Background.rect)

        self.stage_field.stage_rebuild()
        self.prota.moving()
        
        for k in self.enemy_list:                       
            pre_pos_x = k.pos_x
            pre_pos_y = k.pos_y

            for l in self.enemy_list:
                if (k.name != l.name) and (k.pos_x == l.pos_x and k.pos_x == l.pos_y):
                        k.pos_x = pre_pos_x
                        k.pos_y = pre_pos_y
            k.moving()
        
        pygame.display.update()

        End = False

        while not End:

            if len(self.enemy_list) == 0:
                self.ending()

            if len(self.enemy_list) == 0:
                pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    End = True
                    sys.exit()

                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_s or event.key == pygame.K_w or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP):
                    exit = False

                    move_Background=ScreenObject("img",r"image\background\battle screen background.png",pos_x = 809,pos_y=500)
                    screen.blit(move_Background.img,move_Background.rect)

                    self.stage_field.stage_rebuild()
                    if event.key == pygame.K_a and self.prota.pos_y > 0 or event.key == pygame.K_LEFT and self.prota.pos_y > 0:
                        self.prota.pos_y -= 1
                    
                    elif event.key == pygame.K_d and self.prota.pos_y < self.stage_field.size_y-1 or event.key == pygame.K_RIGHT and self.prota.pos_y < self.stage_field.size_y-1:
                        self.prota.pos_y += 1
                    
                    elif event.key == pygame.K_s and self.prota.pos_x < self.stage_field.size_x-1 or event.key == pygame.K_DOWN and self.prota.pos_x < self.stage_field.size_x-1:
                        self.prota.pos_x += 1
                    
                    elif event.key == pygame.K_w and self.prota.pos_x > 0 or event.key == pygame.K_UP and self.prota.pos_x > 0:
                        self.prota.pos_x -= 1

                    ##
                    else:
                        continue

 
                    self.fight()


                    if exit == True:
                        break

                    for k in self.enemy_list:                       
                        pre_pos_x = k.pos_x
                        pre_pos_y = k.pos_y

                        moving_random_value = random.randint(0,3)
                        #print("{} moving value:{}".format(k.name,moving_random_value))
                        if moving_random_value == 0 and k.pos_y > 0:
                            k.pos_y -= 1
                        
                        elif moving_random_value == 1 and k.pos_y < self.stage_field.size_y-1:
                            k.pos_y += 1
                        
                        elif moving_random_value == 2 and k.pos_x < self.stage_field.size_x-1:
                            k.pos_x += 1
                        
                        elif moving_random_value == 3 and k.pos_x > 0:
                            k.pos_x -= 1

                        for l in self.enemy_list:
                            if (k.name != l.name) and (k.pos_x == l.pos_x and k.pos_x == l.pos_y):
                                    k.pos_x = pre_pos_x
                                    k.pos_y = pre_pos_y
                        k.moving()
                        
                        self.fight()

                    print()
                    self.prota.moving()

