# Connect4 AI 
# Author: Sehbazz Virk
# 
# Written January 2021

class Board:
    
    def __init__(self, player1, player2):
        
        self.currentState = [[0 for _ in range(7)] for _ in range(7)]
        self.heights = [0 for _ in range(7)]
        self.symbolP1 = player1
        self.symbolP2 = player2
    
    def getState(self):
        return(self.currentState)
    
    def isValidMove(self, pos):
        
        if self.currentState[0][pos] != 0:
            return False
        else:
            return True
    
    def setMove(self, pos, player):
        
        self.currentState[6-self.heights[pos]][pos] = player
        
        self.heights[pos] += 1
    
    def render(self):
        
        chars = {
            1: self.symbolP1,
            -1: self.symbolP2,
            0: "-"
            }
        
        str_line = "---------------------------------"
        
        print("\n" + str_line)
        for row in self.currentState:
            for cell in row:
                symbol = chars[cell]
                print(f'| {symbol} |', end='')
            print('\n' + str_line)
    
    def gameOver(self):
        
        over = self.checkWinner(1) or self.checkWinner(-1)
    
        return over
    
    
    
    def checkWin(self,row,col,player):
        
        try:
            if (self.currentState[row-1][col] == player 
                and self.currentState[row-2][col] == player 
                and self.currentState[row-3][col] == player):
                return True
        except:
            pass
        
        try:
            if (self.currentState[row-1][col+1] == player 
                    and self.currentState[row-2][col+2] == player 
                    and self.currentState[row-3][col+3] == player):
                return True
        except:
            pass        
        
        try:
            if (self.currentState[row][col+1] == player 
                    and self.currentState[row][col+2] == player 
                    and self.currentState[row][col+3] == player):
                return True
        except:
            pass
        
        try:
            if (self.currentState[row+1][col+1] == player 
                    and self.currentState[row+2][col+2] == player 
                    and self.currentState[row+3][col+3] == player):
                return True
        except:
            pass        
        
        try:
            if (self.currentState[row+1][col] == player 
                    and self.currentState[row+2][col] == player 
                    and self.currentState[row+3][col] == player):
                return True
        except:
            pass        
        
        try:
            if (self.currentState[row+1][col-1] == player 
                    and self.currentState[row+2][col-2] == player 
                    and self.currentState[row+3][col-3] == player):
                return True
        except:
            pass        
        
        try:
            if (self.currentState[row][col-1] == player 
                    and self.currentState[row][col-2] == player 
                    and self.currentState[row][col-3] == player):
                return True
        except:
            pass 
        
        try:
            if (self.currentState[row-1][col-1] == player 
                    and self.currentState[row-2][col-2] == player 
                    and self.currentState[row-3][col-3] == player):
                return True
        except:
            pass        
        
    
    def checkWinner(self,player):

        for row in range(7):
            for col in range(7):
                if self.currentState[row][col] == player:
                    won = self.checkWin(row,col,player)
                    if won:
                        return True

        return False    
        
        
        
        
        
        
        