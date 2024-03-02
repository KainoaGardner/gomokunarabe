import pygame

class Board():

    def __init__(self,WIDTH, EYEAMOUNT,MARGIN,screen):
        self.width = WIDTH
        self.eyeAmount = EYEAMOUNT
        self.margin = MARGIN
        self.eyeGap = (self.width - self.margin * 2)// (EYEAMOUNT - 1)
        self.board = []
        self.blackTurn = True
        self.moveList = []
        self.placeActive = True
        self.font = pygame.font.SysFont("font/8bitfont.tff",75)
        self.screen = screen
        self.winList = []
        self.blackScore = 0
        self.whiteScore = 0

    def drawBoard(self,screen):
        for r in range(self.eyeAmount - 1):
            for c in range(self.eyeAmount - 1):
                pygame.draw.rect(screen,"black",(r*self.eyeGap + self.margin,c*self.eyeGap + self.margin,self.eyeGap,self.eyeGap),2)

    def drawStone(self,screen):
        for r in range(self.eyeAmount):
            for c in range(self.eyeAmount):
                pos = (self.margin + r * self.eyeGap,self.margin + c * self.eyeGap)
                if self.board[r][c] == 1:
                    pygame.draw.circle(screen,"Black",pos,self.eyeGap / 2)
                elif self.board[r][c] == 2:
                    pygame.draw.circle(screen,"White",pos,self.eyeGap / 2)

    def createBoard(self):
        for r in range(self.eyeAmount):
            row = []
            for c in range(self.eyeAmount):
                row.append(0)
            self.board.append(row)

    def placeStone(self,x,y):
        if self.placeActive:
            if self.board[x][y] == 0:
                if self.blackTurn:
                    self.board[x][y] = 1
                else:
                    self.board[x][y] = 2
                self.moveList.append([x,y])
                self.checkWin()
                self.blackTurn = not self.blackTurn

    def undo(self):
        if self.placeActive == False:
            self.winList = []
            self.placeActive = True
        if len(self.moveList) > 0:
            self.board[self.moveList[-1][0]][self.moveList[-1][1]] = 0
            self.moveList.pop(-1)
            self.blackTurn = not self.blackTurn

    def checkWin(self):
        if self.blackTurn:
            turn = 1
        else:
            turn = 2

        for c in range(self.eyeAmount):
            for r in range(self.eyeAmount):
                if self.board[c][r] == turn:
                    if c - 2 >= 0 and c + 2 < self.eyeAmount:
                        if self.board[c - 1][r] == turn and self.board[c - 2][r] == turn and self.board[c + 1][r] == turn and self.board[c + 2][r] == turn:
                            self.winList.append([c - 2,r])
                            self.winList.append([c - 1,r])
                            self.winList.append([c,r])
                            self.winList.append([c + 1,r])
                            self.winList.append([c + 2,r])
                    if r - 2 >= 0 and r + 2 < self.eyeAmount:
                        if self.board[c][r -1] == turn and self.board[c][r - 2] == turn and self.board[c][r + 1] == turn and self.board[c][r +2] == turn:
                            self.winList.append([c,r-2])
                            self.winList.append([c,r-1])
                            self.winList.append([c,r])
                            self.winList.append([c,r+1])
                            self.winList.append([c,r+2])
                    if c - 2 >= 0 and c + 2 < self.eyeAmount and r - 2 >= 0 and r + 2 < self.eyeAmount:
                        if self.board[c-1][r-1] == turn and self.board[c-2][r-2] == turn and self.board[c+1][r+1] == turn and self.board[c+2][r+2] == turn:
                            self.winList.append([c-2,r-2])
                            self.winList.append([c - 1,r - 1])
                            self.winList.append([c,r])
                            self.winList.append([c+1,r+1])
                            self.winList.append([c+2,r+2])
                        if self.board[c+1][r-1] == turn and self.board[c+2][r-2] == turn and self.board[c-1][r+1] == turn and self.board[c-2][r+2] == turn:
                            self.winList.append([c + 2,r - 2])
                            self.winList.append([c + 1,r - 1])
                            self.winList.append([c, r])
                            self.winList.append([c - 1,r + 1])
                            self.winList.append([c - 2,r + 2])
        if len(self.winList) > 0:
            if turn == 1:
                self.blackScore += 1
            if turn == 2:
                self.whiteScore += 1

    def drawWinner(self,screen):
        if len(self.winList) > 0:
            self.placeActive = False

            if not self.blackTurn:
                text = self.font.render(f"Black Wins! {self.blackScore}", False, "Black")
                textRect = text.get_rect(center = (self.width/2,self.margin/2))
                screen.blit(text,textRect)
                restartText = self.font.render("SPACE to Restart!", False, "Black")
                restartTextRect = restartText.get_rect(center=(self.width / 2, self.width - self.margin / 2))
                screen.blit(restartText, restartTextRect)
                for pos in self.winList:
                    pos = (self.margin + pos[0] * self.eyeGap,self.margin + pos[1] * self.eyeGap)
                    pygame.draw.circle(screen,"#fdcb6e",pos,self.eyeGap/2)
                    pygame.draw.circle(screen, "Black", pos, self.eyeGap / 2 - 5)
            else:

                text = self.font.render(f"White Wins! {self.whiteScore}", False, "White")
                textRect = text.get_rect(center=(self.width / 2, self.margin / 2))
                screen.blit(text, textRect)
                restartText = self.font.render("SPACE to Restart!", False, "White")
                restartTextRect = restartText.get_rect(center=(self.width / 2, self.width - self.margin / 2))
                screen.blit(restartText, restartTextRect)
                for pos in self.winList:
                    pos = (self.margin + pos[0] * self.eyeGap, self.margin + pos[1] * self.eyeGap)
                    pygame.draw.circle(screen, "#fdcb6e",pos,self.eyeGap/2)
                    pygame.draw.circle(screen,"White",pos,self.eyeGap/2 - 5)

    def restart(self):
        self.winList = []
        self.blackTurn = True
        self.moveList = []
        self.placeActive = True
        self.board = []
        self.createBoard()