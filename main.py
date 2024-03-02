import pygame
from board import Board

pygame.init()
WIDTH = 800
HEIGHT = 800
EYEAMOUNT = 9   #19, 13, 9
MARGIN = 50
EYEGAP = (WIDTH - MARGIN * 2) // EYEAMOUNT

screen = pygame.display.set_mode((WIDTH,HEIGHT))
board = Board(WIDTH,EYEAMOUNT,MARGIN,screen)

def main():
    running = True
    board.createBoard()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if MARGIN <= x <= WIDTH - MARGIN and MARGIN <= y <= HEIGHT - MARGIN:
                    fullEyeGap = (WIDTH - MARGIN * 2 + EYEGAP) // EYEAMOUNT
                    x -= MARGIN
                    y -= MARGIN
                    x = round(x / fullEyeGap)
                    y = round(y / fullEyeGap)
                    if x <= EYEAMOUNT - 1 and y <= EYEAMOUNT - 1:
                        board.placeStone(x,y)
            elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_r:
                board.undo()
             if event.key == pygame.K_SPACE:
                 board.restart()


        screen.fill("#c19a6b")
        board.drawBoard(screen)
        board.drawStone(screen)
        board.drawWinner(screen)
        pygame.display.update()
main()