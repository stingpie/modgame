#that dream I had
from PIL import Image as image
import pygame, time, numpy


def listtest(val1,array):
    for i in range(len(array)):
        if val1==array[i]:
            return True
    return False

class actor:
    def __init__(self,name,pos,spr):
        global actornum
        actornum+=1
        self.name = name #actor's name
        self.vec = [0,0] #Vector movement (x,y)
        self.pos = pos #position pair (x,y)
        self.spr = spr #sprite number (x)
        self.facing = "right"
        self.gravity = True
        self.drag = 0.01
        self.friction = 0.02
        self.bounce = 0
        self.entering=False
    def collide(self):
         global world
         global currentworld
         if self.vec[1]+player.pos[1]>yscale*8 or self.vec[0]+player.pos[0]>xscale*8:
             self.vec[0]=0
             self.vec[1]=0
            #loading zones
         if self.facing=="right" and self.entering==False:
             if (self.collidetest((0,0),(-1,0))>100 and self.collidetest((0,0),(-1,0))<200) or (self.collidetest((0,1),(-1,0))>100 and self.collidetest((0,1),(-1,0))<200):


                print(self.collidetest((0,0),(-1,0)))
                print(self.collidetest((0,1),(-1,0)))


                z=self.collidetest((0,0),(-1,0))
                print(z)
                im=image.open("maps\\MAP"+str(z-101)+".bmp","r")
                world=im.load()
                player.pos=self.world_search(z,currentworld)
                currentworld=z
                self.entering=True
         if self.facing=="left" and self.entering==False:
             if(self.collidetest((1,0),(1,0))>100 and self.collidetest((1,0),(1,0))<200) or (self.collidetest((1,1),(1,0))>100 and self.collidetest((1,1),(1,0))<200):
                z=self.collidetest((1,0),(1,0))
                im=image.open("maps\\MAP"+str(z-101)+".bmp","r")
                world=im.load()
                player.pos=self.world_search(z,currentworld)
                currentworld=z
                self.entering=True
         if not((self.collidetest((1,0),(1,0))>100 or self.collidetest((1,1),(1,0))>100) and (self.collidetest((1,0),[1,0])<200 or self.collidetest((1,1),[1,0])<200)) and not((self.collidetest((0,0),(-1,0))>100 or self.collidetest((0,1),(-1,0))>100) and (self.collidetest((0,0),(-1,0))<200 or self.collidetest((0,1),(-1,0))<200)) and not (self.collidetest((0.5,0.5),(0,0))>100 and self.collidetest((0.5,0.5),(0,0))<200):
            
             self.entering=False

         if ((listtest(self.collidetest((0,1),(0,1)),collision) or listtest(self.collidetest((1,1),(0,1)),collision))) and self.vec[1]==0 :
             self.pos[1]= int(self.pos[1]*(zoomy/yscale))/(zoomy/yscale)
             
            
        #left-right collision
         if listtest(self.collidetest((1.01,0),(1,0)),collision) or listtest(self.collidetest((1.01,0.999),(1,0)),collision):

           if self.bounce != 0:
                   self.vec[0]*=-self.bounce
           if self.vec[0] < 0:
               self.vec[0] = 0
            
         if listtest(self.collidetest((-0.01,0),(-1,0)),collision) or  listtest(self.collidetest((-0.01,0.999),(-1,0)),collision):

           if self.bounce != 0:
                   self.vec[0]*=-self.bounce
           if self.vec[0] > 0:
               self.vec[0] = 0
         self.pos[0]+=self.vec[0]
        #down collision
         if self.collidetest((0,1),(0,1))==255 or self.collidetest((1,1),(0,1))==255:

           if self.friction != 0:
               self.vec[0] *= 1-self.friction

           if self.vec[1] != 0:

               if self.bounce != 0:

                   self.vec[1]*=-self.bounce
                   
               else:

                   self.vec[1] = 0
         elif self.collidetest((0,1),(0,1))==0 or self.collidetest((1,1),(0,1))==0:
             
           if jumpticks<1 and player == self: 
               self.vec[1] += 0.80/(yscale)
           elif (not jumpticks<1) and player == self:
               self.vec[1] += 0.1/(yscale)

               
           if self.gravity:    
               self.vec[1] *= 1 - self.drag
               
           self.pos[1] += self.vec[1]
         elif self.collidetest(1)==100:

             self.vec[1]*=0.99
             self.pos[1] += self.vec[1]
             self.vec[0] *= 1-self.friction
         elif self.collidetest(1)==200:

             self.vec[1]*=-1
             self.pos[1] += self.vec[1]
             self.vec[0] *= 1-self.friction
         
        ##up collision
         if listtest(self.collidetest((0,0),(0,-1)),collision) or listtest(self.collidetest((1,0),(0,-1)),collision):
            if self.bounce != 0:
                   self.vec[1]*=-self.bounce
            if self.vec[1] < 0:
                self.vec[1] = 0
         if self.name=="bullet" and self.vec[0]==0:
             return

         return self

    def collidetest(self,addpos,direc):
        pos2=[0,0]
        pos2[0]=addpos[0]
        pos2[1]=addpos[1]
        
            
        posx=self.pos[0]*(xscale/winx)
        posy=self.pos[1]*(yscale/winy)*2.53
        vecx=self.vec[0]*(xscale/winx)
        vecy=self.vec[1]*(yscale/winy)*2.53
        return world[int(posx+pos2[0]+(vecx*direc[0])),int(posy+pos2[1]+(vecy*direc[1]))][0]

    
    def world_search(self,nadress,xadress):

        worldn=image.open("maps\\MAP"+str(nadress-101)+".bmp","r")
        posx=self.pos[0]*(xscale/winx)
        posy=self.pos[1]*(yscale/winy)
        candidates=[]
        candidates2=[]
        world2=worldn.load()

        for x in range(worldn.size[0]):
            for y in range(worldn.size[1]):
                if world2[x,y][0]==xadress:
                    if world2[x,y+1][0] != xadress:
                        candidates=candidates+[[x,y]]
            
        if len(candidates)!=0:
            for i in range(len(candidates)):

                    candidates2=numpy.append(candidates2,abs((posx-candidates[i][0])+(posy-candidates[i][1])))         
            z=candidates[numpy.argmin(candidates2)]
  
            z[0]=(z[0]+numpy.sign(self.vec[0])*0)*(winx/xscale)
            z[1]=z[1]*(winx/xscale)
        else:
            z=[8,8]
        return z

def initialize():
    pygame.display.init()
    global world
    global window
    global winx
    global winy
    global sprites
    global xscale #the num of pixels in the map
    global yscale #the num of pixels in the map
    global wallimg
    global actornum
    global projectile
    global wallimg2
    global currentworld
    currentworld=101
    projectile=[]
    actornum=0
    im=image.open("maps\\MAP0.bmp","r")
    xscale=im.size[0]
    yscale=im.size[1]
    sprites=[]
    for i in range(2):
        sprites=numpy.append(sprites,pygame.image.load("Tiles\\sprite"+str(i)+".bmp","r" ))
        sprites[i].set_colorkey(pygame.Color(255,0,255))
    


    wallimg=[]
    wallimg2=[]
    for i in range(4):
        wallimg=numpy.append(wallimg,pygame.image.load("Tiles\\tile"+str(i)+".bmp","r"))
        wallimg2=numpy.append(wallimg2,pygame.transform.scale(pygame.image.load("Tiles\\tile"+str(i)+".bmp","r"),(int(winx/xscale),int(winy/yscale))))
    
    world=im.load()

    pygame.init()
    window=pygame.display.set_mode((winx,winy))


    

def simpledraw():
    global zoomy
    global zoomx
    global campos
    global wallimg2
    campos[0]=(campos[0])*(zoomx/winx)-winx/2 +16
    campos[1]=(campos[1])*(zoomx/winx)-winx/2 +16
    if zoomx/xscale!=wallimg2[0].get_height():
        for i in range(len(wallimg)):
            wallimg2[i]=pygame.transform.scale(wallimg[i],(int(zoomx/xscale),int(zoomy/yscale)))

    for x in range(xscale):
        for y in range(yscale):
            factorx=zoomx/xscale
            factory=zoomx/xscale
            window.blit(wallimg2[world[x,y][1]],(x*factorx-campos[0],y*factory-campos[1]))

    for i in range(len(projectile)):
        
        window.blit(pygame.transform.scale(sprites[projectile[i].spr],(int(zoomx/xscale),int(zoomx/xscale))),(projectile[i].pos[0]+(xscale/2)-campos[0],projectile[i].pos[1]+(xscale/2)-campos[1]))
        
    window.blit(pygame.transform.scale(sprites[0],(int(zoomx/xscale),int(zoomx/xscale))),(player.pos[0]*zoomx/(winx) - campos[0],player.pos[1]*zoomx/(winx) - campos[1]))



def control():
     global jumpticks
     global projectile
     global spacetimer
     global zoomx
     global zoomy
     
     key=pygame.key.get_pressed()
     if key[pygame.K_RIGHT] :
         player.facing="right"
         player.vec[0]+=0.8/xscale

     if key[pygame.K_LEFT] :
         player.facing="left"
         player.vec[0]-=0.8/xscale

     if key[pygame.K_LEFT] or key[pygame.K_RIGHT]:
         player.friction=0.01
     else:
         player.friction=0.2

     if key[pygame.K_UP] and (listtest(player.collidetest((0,1),(0,1)),collision) or listtest(player.collidetest((1,1),(0,1)),collision) ) :
         jumpticks=50
     if jumpticks>0:    
         jumpticks-=1
     
     if key[pygame.K_UP] and (listtest(player.collidetest((0,1),(0,1)),collision) or listtest(player.collidetest((1,1),(0,1)),collision) and not (listtest(player.collidetest((0,0),(0,-1)),collision) or listtest(player.collidetest((1,0),(0,-1)),collision))):
        player.vec[1]-=32/yscale
        player.pos[1]-=1
     if not key[pygame.K_UP] and not (listtest(player.collidetest((0,1),(0,1)),collision) or listtest(player.collidetest((1,1),(0,1)),collision)):
         jumpticks=0
     if player.collidetest((0,1),(0,1))==100 or player.collidetest((1,1),(0,1)):
        if key[pygame.K_UP]:
            player.vec[1]=-8/yscale
            
        elif key[pygame.K_DOWN]:
            player.vec[1]=8/yscale


            
            
     if key[pygame.K_SPACE]:
         if spacetimer==0:
             projectile=numpy.append(projectile,actor("bullet",player.pos[:],1))
             spacetimer=25
             projectile[-1:][0].gravity = False
             projectile[-1:][0].facing = player.facing
             if projectile[-1:][0].facing=="right":
                 projectile[-1:][0].vec[0] = 10
             if projectile[-1:][0].facing=="left":
                 projectile[-1:][0].vec[0] = -10
     else:
         spacetimer=0
     if spacetimer>0:
         spacetimer-=1
     if key[pygame.K_e] :
         zoomx*=1.1
         zoomy*=1.1
     if key[pygame.K_q] :
         zoomx/=1.1
         zoomy/=1.1

closing=False
winx=400 #Actuall window size
winy=400 #actuall window size
zoomx=winx*3 #size of a virtual window (aka the num of pixels zoomed in it is)
zoomy=winy*3 #size of a virtual window (aka the num of pixels zoomed in it is)
initialize()
player=actor("player",[8,8],0)
player.vec=[0,0]
jumpticks=0
collision=[255,200]
spacetimer=0
campos=[0,0]

while not closing:
    pygame.event.pump()
    pygame.display.flip()
    control()
    player=player.collide()

    for i in range(len(projectile)):
        quicktest=projectile[len(projectile)-i-1].collide()
        if quicktest != None:
            projectile[len(projectile)-i-1]=quicktest
        else:
            projectile=numpy.append(projectile[:len(projectile)-i-1],projectile[len(projectile)-i:])
    campos[0]=player.pos[0] 
    campos[1]=player.pos[1] 
    time.sleep(0.01)
    pygame.draw.rect(window,(0,0,0),(0,0,winx,winy))
    simpledraw()

