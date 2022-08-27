import pygame              

screen_width = 600        
screen_height = 400      
screen = pygame.display.set_mode((screen_width, screen_height))

card0 = pygame.image.load("card1.png")
card1 = pygame.image.load("card2.png")
cardback = pygame.image.load("cardback.png")
cardList = [card0, card1]
rect_card0 = card0.get_rect()
rect_card1 = card1.get_rect()
rect_cardback = cardback.get_rect()

cardList_rect = [rect_card0,rect_card1]

rect_card0.topleft = (100,100)
rect_card1.topleft = (300,100)
rect_cardback.topleft = (500,100)


running = True              
while running:
       for event in pygame.event.get():         
              if event.type == pygame.QUIT:             
                     running = False           

              elif event.type == pygame.MOUSEBUTTONDOWN:
                     
              
                     if rect_cardback.collidepoint(event.pos):
                            print('oooo')
                            
                            #rect_cardback.fill((0,0,0,0))
                     else:
                            print('xxxxx')
              '''
              for i in cardList_rect:
                     if i.collidepoint(event.pos):
                            aa= False
                            #if i in cardList_rect:
                                   #aa= False
                           # else :
                                   #aa= True
                     else:
                            aa= True
                            #print(cardList_rect.index(i))
              '''
             

       screen.blit(cardList[0], (100, 100))
       screen.blit(cardList[1], (300, 100))
       screen.blit(cardback, (500, 100))
       pygame.display.update() 

pygame.quit()