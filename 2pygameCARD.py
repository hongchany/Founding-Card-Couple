import pygame               #모듈 불러오기
import random
import time

pygame.init()               #초기화

# 화면 크기 설정
screen_width = 950          # 가로 
screen_height = 800         # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 회면 타이틀 설정
pygame.display.set_caption("LOOK FOR CARD")               # 게임 이름
backgound = (60, 120, 65)

def randomCard():
       li=[]
       while len(li) < 6:
              a = random.randint(0,5)
              if not(a in li):
                     li.append(a)
       return li

def randomCard2(n, m):
       li=[]
       for i in range(n, m):
              for j in range(6):
                     li.append((i,j))
       random.shuffle(li)
       return li

startPosition = (50, 50)

# 카드 이미지 불러오기
card0 = pygame.image.load("card1.png")
card1 = pygame.image.load("card2.png")
card2 = pygame.image.load("card3.png")
card3 = pygame.image.load("card4.png")
card4 = pygame.image.load("card5.png")
card5 = pygame.image.load("card6.png")
card6 = pygame.image.load("card7.png")
card7 = pygame.image.load("card8.png")
card8 = pygame.image.load("card9.png")
card9 = pygame.image.load("card10.png")
card10 = pygame.image.load("card11.png")
card11 = pygame.image.load("card12.png")
cardback = pygame.image.load("cardback.png")

#  카드 이미지 리스트(변수 뒤 숫자 = 하드게임에 사용될 복제된 카드리스트)
cardList = [card0, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11]
cardList2 = [card0, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11]

randomList_x_up = randomCard()
randomList_x_down = randomCard()

randomList2_up = randomCard2(0, 2)
randomList2_down = randomCard2(2, 4)

rectList = []               #카드의 좌표 리스트
rectList2 = []

finishCard = []             #완성된 카드 리스트

choiceCard = -1             # 선택한 카드의 리스트 주소를 담을 변수 
choiceCard2 = -1

delayCount = 0                     # 카드가 불일치할 때 쓰이는 지연 변수

#카드의 좌표를 하나씩 넣어줄 포문
for i in cardList:
       rectList.append(i.get_rect())

for j in cardList2:
       rectList2.append(j.get_rect())

def cardArrange(choice):
       if choice == 1:
              for y in range(2):
                     for x in range(6):
                            if y == 0:
                                   screen.blit(cardList[x], (startPosition[0]+150*randomList_x_up[x], startPosition[1]+183*y+200))
                                   rectList[x].topleft = (startPosition[0]+150*randomList_x_up[x], startPosition[1]+183*y+200)
                                   screen.blit(cardback, (startPosition[0]+150*randomList_x_up[x], startPosition[1]+183*y+200))
                            else:
                                   screen.blit(cardList2[x], (startPosition[0]+150*randomList_x_down[x], startPosition[1]+183*y+200))
                                   rectList2[x].topleft = (startPosition[0]+150*randomList_x_down[x], startPosition[1]+183*y+200)
                                   screen.blit(cardback, (startPosition[0]+150*randomList_x_down[x], startPosition[1]+183*y+200))
       else:
              for y in range(4):
                     for x in range(12):
                            if y == 0 or y==1 :
                                   screen.blit(cardList[x], (startPosition[0]+150*randomList2_up[x][1], startPosition[1]+183*randomList2_up[x][0]))
                                   rectList[x].topleft = (startPosition[0]+150*randomList2_up[x][1], startPosition[1]+183*randomList2_up[x][0])
                                   screen.blit(cardback, (startPosition[0]+150*randomList2_up[x][1], startPosition[1]+183*randomList2_up[x][0]))
                            if y == 2 or y == 3:
                                   screen.blit(cardList2[x], (startPosition[0]+150*randomList2_down[x][1], startPosition[1]+183*randomList2_down[x][0]))
                                   rectList2[x].topleft = (startPosition[0]+150*randomList2_down[x][1], startPosition[1]+183*randomList2_down[x][0])
                                   screen.blit(cardback, (startPosition[0]+150*randomList2_down[x][1], startPosition[1]+183*randomList2_down[x][0]))

def oneCard(cardNumber):
       if cardNumber>=0:
              screen.blit(cardList[cardNumber], (startPosition[0]+150*randomList2_up[cardNumber][1], startPosition[1]+183*randomList2_up[cardNumber][0]))

def oneCard2(cardNumber):
       if cardNumber>=0:
              screen.blit(cardList2[cardNumber], (startPosition[0]+150*randomList2_down[cardNumber][1], startPosition[1]+183*randomList2_down[cardNumber][0]))

def endCard():
       for i in finishCard:
              screen.blit(cardList[i], (startPosition[0]+150*randomList2_up[i][1], startPosition[1]+183*randomList2_up[i][0]))
              
              screen.blit(cardList2[i], (startPosition[0]+150*randomList2_down[i][1], startPosition[1]+183*randomList2_down[i][0]))
       
def wholeBack(choice):
       if choice == 1:
              for y in range(2):
                     for x in range(6):
                            if y == 0:
                                   screen.blit(cardback, (startPosition[0]+150*randomList_x_up[x], startPosition[1]+183*y+200))
                            else:
                                   screen.blit(cardback, (startPosition[0]+150*randomList_x_down[x], startPosition[1]+183*y+200))
       else:
              for y in range(4):
                     for x in range(12):
                            if y == 0 or y==1 :
                                   screen.blit(cardback, (startPosition[0]+150*randomList2_up[x][1], startPosition[1]+183*randomList2_up[x][0]))
                            if y == 2 or y == 3:
                                   screen.blit(cardback, (startPosition[0]+150*randomList2_down[x][1], startPosition[1]+183*randomList2_down[x][0]))

# 이벤트 루프
running = True              # 게임이 진행 중인가?
while running:
       for event in pygame.event.get():          # 어떤 이벤트가 발생하였는가?
              if event.type == pygame.QUIT:             # 창이 단히는 이벤트가 발생하였는가?
                     running = False             # 게임이 진행 중이 아님
              elif event.type == pygame.MOUSEBUTTONDOWN:              # 마우스 버튼이 눌렸을 때
                     delayCount += 1
                     if delayCount == 2:
                            time.sleep(0.5)
                            delayCount = 0
                     for i in rectList:
                            if i.collidepoint(event.pos):
                                   print(rectList.index(i))                  
                                   # screen.blit(cardList[i], (startPosition[0]+150*randomList2_up[i][1], startPosition[1]+183*randomList2_up[i][0]))
                                   choiceCard = rectList.index(i)                   # 1번 카드좌표리스트 좌표의 클릭한 카드 주소를 변수에 담음  
                     for i in rectList2:
                            if i.collidepoint(event.pos):
                                   print(rectList2.index(i))
                                   # screen.blit(cardList2[i], (startPosition[0]+150*randomList2_down[i][1], startPosition[1]+183*randomList2_down[i][0]))
                                   choiceCard2 = rectList2.index(i)                 # 2번 카드좌표리스트 좌표의 클릭한 카드 주소를 변수에 담음
                     
       screen.fill(backgound)
       cardArrange(2)
       wholeBack(2)
       endCard()

       print(delayCount)
       
       oneCard(choiceCard)
       oneCard2(choiceCard2)

       if(choiceCard == choiceCard2) and (choiceCard != -1) :
              finishCard.append(choiceCard)

       endCard()

       pygame.display.update() 

pygame.quit()



