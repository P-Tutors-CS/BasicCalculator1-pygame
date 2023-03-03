import pygame, sys, random
import os
from pygame.locals import QUIT
from pygame import mixer
from basicCalculator import *;
# Initializing Pygame
pygame.init()

# golbal variables
WIDTH, HEIGHT = 482, 360  #macth scratch screen dimensions
digitX, digitY = 465,10
resultX,resultY = 465,42
operator ,currNum = "", ""
num1, num2 = 0, 0

wood_tap_sound = mixer.Sound("WoodTap.mp3")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
ORANGE = (255, 165, 0)
ORANGE = (255, 140, 0)# dark

FRAMES_PER_SEC = 60

num = str( random.randint(1, 3))
BACKGROUND_IMAGE = pygame.image.load(os.path.join("Images_png", num+".png"))

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Calculator!")


# create rects to act as buttons
ZERO = pygame.Rect(10,300,112,45)
ZERO_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
ZERO_SURFACE.fill((0, 0, 0, 50))                         # notice the alpha value in the color

DOT = pygame.Rect(130,300,112,45)
DOT_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
DOT_SURFACE.fill((0, 0, 0, 50)) 

EQUAL = pygame.Rect(249,300,112,45)
EQUAL_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
EQUAL_SURFACE.fill((0, 0, 0, 50)) 

PLUS = pygame.Rect(364,300,112,45)
PLUS_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
PLUS_SURFACE.fill((0, 0, 0, 50)) 

ONE = pygame.Rect(10,250,112,45) 
ONE_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
ONE_SURFACE.fill((0, 0, 0, 50)) 

TWO = pygame.Rect(130,250,112,45)
TWO_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
TWO_SURFACE.fill((0, 0, 0, 50)) 

THREE = pygame.Rect(246,250,112,45)  
THREE_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
THREE_SURFACE.fill((0, 0, 0, 50)) 

MINUS = pygame.Rect(364,250,112,45)
MINUS_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
MINUS_SURFACE.fill((0, 0, 0, 50)) 

FOUR = pygame.Rect(10,199,112,45)#195
FOUR_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
FOUR_SURFACE.fill((0, 0, 0, 50)) 

FIVE = pygame.Rect(130,199,112,45)
FIVE_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
FIVE_SURFACE.fill((0, 0, 0, 50)) 

SIX = pygame.Rect(246,199,112,45)
SIX_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
SIX_SURFACE.fill((0, 0, 0, 50)) 

MULTIPLY = pygame.Rect(364,199,112,45)
MULTIPLY_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
MULTIPLY_SURFACE.fill((0, 0, 0, 50)) 


SEVEN = pygame.Rect(10,145,112,45)
SEVEN_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
SEVEN_SURFACE.fill((0, 0, 0, 50)) 

EIGHT = pygame.Rect(130,145,112,45)
EIGHT_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
EIGHT_SURFACE.fill((0, 0, 0, 50))  

NINE = pygame.Rect(246,145,112,45)  
NINE_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
NINE_SURFACE.fill((0, 0, 0, 50)) 

DIVIDE = pygame.Rect(364,145,112,45)
DIVIDE_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
DIVIDE_SURFACE.fill((0, 0, 0, 50)) 


CLEAR = pygame.Rect(364,95,112,45)
CLEAR_SURFACE = pygame.Surface((112,45), pygame.SRCALPHA)   # per-pixel alpha
CLEAR_SURFACE.fill((0, 0, 0, 50)) 


# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)
font.render("", True, BLACK)

digitBuilder = ""
resultBuilder = ""
 

def setup():
  DISPLAYSURF.blit(BACKGROUND_IMAGE, (0,0))
  
  DISPLAYSURF.blit(ZERO_SURFACE, (ZERO.x,ZERO.y))
  # pygame.draw.rect(DISPLAYSURF, GREEN, ZERO,2)

  DISPLAYSURF.blit(DOT_SURFACE, (DOT.x,DOT.y))
  DISPLAYSURF.blit(EQUAL_SURFACE, (EQUAL.x,EQUAL.y))
  DISPLAYSURF.blit(PLUS_SURFACE, (PLUS.x,PLUS.y))
  # DISPLAYSURF.blit(ZERO_SURFACE, (15,300))
  
  DISPLAYSURF.blit(ONE_SURFACE, (ONE.x,ONE.y))
  DISPLAYSURF.blit(TWO_SURFACE, (TWO.x,TWO.y))
  DISPLAYSURF.blit(THREE_SURFACE, (THREE.x,THREE.y))
  DISPLAYSURF.blit(MINUS_SURFACE, (MINUS.x,MINUS.y))

  DISPLAYSURF.blit(FOUR_SURFACE, (FOUR.x,FOUR.y))
  DISPLAYSURF.blit(FIVE_SURFACE, (FIVE.x,FIVE.y))
  DISPLAYSURF.blit(SIX_SURFACE, (SIX.x,SIX.y))
  DISPLAYSURF.blit(MULTIPLY_SURFACE, (MULTIPLY.x,MULTIPLY.y))


  DISPLAYSURF.blit(SEVEN_SURFACE, (SEVEN.x,SEVEN.y))
  DISPLAYSURF.blit(EIGHT_SURFACE, (EIGHT.x,EIGHT.y))
  DISPLAYSURF.blit(NINE_SURFACE, (NINE.x,NINE.y))
  DISPLAYSURF.blit(DIVIDE_SURFACE, (DIVIDE.x,DIVIDE.y))

  DISPLAYSURF.blit(CLEAR_SURFACE, (CLEAR.x,CLEAR.y))


def update_elements():
  # copying the text surface object
  # to the display surface object
  # at the center coordinate.
  digitDisplay = font.render(digitBuilder, True, BLACK)
  resultDisplay = font.render(resultBuilder, True, BLACK)
  x = digitDisplay.get_width() ;
  DISPLAYSURF.blit(digitDisplay, (digitX -x, digitY))
  x = resultDisplay.get_width() ;
  DISPLAYSURF.blit(resultDisplay, (resultX-x,resultY))
  pygame.display.update()

def calculate(num1,operator,num2):
  global resultBuilder, digitBuilder
  
  resultBuilder = ""
  if operator == "+":
    resultBuilder = str(add(num1,num2))
  if operator == "-":
    resultBuilder = str(subtract(num1,num2))
  if operator == "x":
    resultBuilder = str(multiply(num1,num2))
  if operator == "÷":
    resultBuilder = str(divide(num1,num2))
  digitBuilder = ""
  
def button_clicked():
    global digitBuilder, digitX,num1,num2,operator, currNum,resultBuilder
    if resultBuilder:
      resultBuilder = ""
    if DOT.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the .")
        digitBuilder += "."
        currNum += "."
        wood_tap_sound.play()

    if ZERO.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the 0")
        wood_tap_sound.play()
        digitBuilder += "0"
        currNum += "0"
    if ONE.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the 1")
        wood_tap_sound.play()
        digitBuilder += "1"
        currNum += "1"
    if TWO.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the 2")
        wood_tap_sound.play()
        digitBuilder += "2"
        currNum += "2"
    if THREE.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the 3")
        wood_tap_sound.play()
        digitBuilder += "3"
        currNum += "3"
    if FOUR.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the 4")
        wood_tap_sound.play()
        digitBuilder += "4"
        currNum += "4"
    if FIVE.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the 5")
        wood_tap_sound.play()
        digitBuilder += "5"
        currNum += "5"
    if SIX.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the 6")
        wood_tap_sound.play()
        digitBuilder += "6"
        currNum += "6"
    if SEVEN.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the 7")
        wood_tap_sound.play()
        digitBuilder += "7"
        currNum += "7"
    if EIGHT.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the 8")
        wood_tap_sound.play()
        digitBuilder += "8"
        currNum += "8"
    if NINE.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the 9")
        wood_tap_sound.play()
        digitBuilder += "9"
        currNum += "9"
    if PLUS.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the +")
        wood_tap_sound.play()
        if digitBuilder and currNum and currNum.replace('.', '', 1).isnumeric():
          num1 = float(currNum)
          operator = "+"
          currNum = ""
        digitBuilder += "+"
    if MINUS.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the -")
        wood_tap_sound.play()
        if digitBuilder and currNum and currNum.replace('.', '', 1).isnumeric():
          num1 = float(currNum)
          operator = "-"
          currNum = ""
        digitBuilder += "-"
    if MULTIPLY.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the X")
        wood_tap_sound.play()
        if digitBuilder and currNum and currNum.replace('.', '', 1).isnumeric():
          num1 = float(currNum)
          operator = "x"
          currNum = ""
        digitBuilder += "x"
    if DIVIDE.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the ÷")
        wood_tap_sound.play()
        if digitBuilder and currNum and currNum.replace('.', '', 1).isnumeric():
          num1 = float(currNum)
          operator = "÷"
          currNum = ""
        digitBuilder += "÷"
    if EQUAL.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the =")
        print(currNum)
        wood_tap_sound.play()
        if digitBuilder and currNum and currNum.replace('.', '', 1).isnumeric():
          num2 = float(currNum)
          currNum = ""
          calculate(num1,operator,num2)
    if CLEAR.collidepoint(pygame.mouse.get_pos()):
        print("Mouse released on the C")
        wood_tap_sound.play()
        digitBuilder = ""
        currNum = ""
        num1=""
        num2 =""

def main():
  clock = pygame.time.Clock()

  while True:
    clock.tick(FRAMES_PER_SEC)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.MOUSEBUTTONUP:
          button_clicked()
    setup()
    update_elements()
    
     
      # pygame.display.update()

if __name__ == "__main__":
    main()