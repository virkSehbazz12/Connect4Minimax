# Connect4 AI 
# Author: Sehbazz Virk
# 
# Written January 2021

import math.inf as infinity


class Board:
    
    def __init__(self):
        self.currentState = [[0 for _ in range(7)] for _ in range(7)]
        self.heights = [0 for _ in range(7)]
    
    def getState(self):
        return(self.currentState)
    
    def isValidMove(self, pos):
        
        if self.currentState[0][pos] != 0:
            return False
        else:
            return True
    
    def setMove(self, pos, player):
        
        self.currentState[self.heights[pos]][pos] = player
        
        self.heights[pos] += 1
    
    def render(self, symbolP1, symbolP2):
        
        chars = {
            -1: symbolP1,
            1: symbolP2,
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
    
    def checkWinner(self,player):
        
        for row in range(7):
            for col in range(7):
                if self.currentState[row][col] == player:
                    won = checkWin(row,col,player)
                    if won:
                        return True
        
        return False
    
    def checkWin(self,row,col,player):
        
        try:
            if (self.currentState[row-1][col] == player 
                and self.currentState[row-2][col] == player 
                and self.currentState[row-3][col] == player):
                return True
        except:
            pass

        
        
        
        
        
        
        
        
        
        