# Connect4 AI 
# Author: Sehbazz Virk
# 
# Written January 2021

class Board:
    
    def __init__(self, player1, player2):
        
        self.currentState = [[0 for _ in range(7)] for _ in range(7)]
        self.heights = [0 for _ in range(7)]
        self.symbolP1 = player1.getSymbol()
        self.symbolP2 = player2.getSymbol()
    
    def getState(self):
        return(self.currentState)
    
    def isValidMove(self, pos):
        
        if self.currentState[0][pos] != 0:
            return False
        else:
            return True
    
    def setMove(self, pos, player):
        
        self.currentState[6-self.heights[pos]][pos] = player.getIdentity()
        
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
    
    def checkWin(self,row,col,identity):
        
        try:
            if (self.currentState[row-1][col] == identity 
                and self.currentState[row-2][col] == identity 
                and self.currentState[row-3][col] == identity):
                return True
        except:
            pass
        
        try:
            if (self.currentState[row-1][col+1] == identity 
                    and self.currentState[row-2][col+2] == identity 
                    and self.currentState[row-3][col+3] == identity):
                return True
        except:
            pass        
        
        try:
            if (self.currentState[row][col+1] == identity 
                    and self.currentState[row][col+2] == identity 
                    and self.currentState[row][col+3] == identity):
                return True
        except:
            pass
        
        try:
            if (self.currentState[row+1][col+1] == identity 
                    and self.currentState[row+2][col+2] == identity 
                    and self.currentState[row+3][col+3] == identity):
                return True
        except:
            pass        
        
        try:
            if (self.currentState[row+1][col] == identity 
                    and self.currentState[row+2][col] == identity 
                    and self.currentState[row+3][col] == identity):
                return True
        except:
            pass        
        
        try:
            if (self.currentState[row+1][col-1] == identity 
                    and self.currentState[row+2][col-2] == identity 
                    and self.currentState[row+3][col-3] == identity):
                return True
        except:
            pass        
        
        try:
            if (self.currentState[row][col-1] == identity 
                    and self.currentState[row][col-2] == identity 
                    and self.currentState[row][col-3] == identity):
                return True
        except:
            pass 
        
        try:
            if (self.currentState[row-1][col-1] == identity 
                    and self.currentState[row-2][col-2] == identity 
                    and self.currentState[row-3][col-3] == identity):
                return True
        except:
            pass        
        
    
    def checkWinner(self,player):
        
        playerIDEN = player.getIdentity()
        
        for row in range(7):
            for col in range(7):
                if self.currentState[row][col] == playerIDEN:
                    won = self.checkWin(row,col,playerIDEN)
                    if won:
                        return True

        return False    
        
        
class Player:
    
    def __init__(self, symbol, identity):
        
        self.symbol = symbol
        self.IDEN = identity
    
    def getSymbol(self):
        
        return self.symbol
    
    def getIdentity(self):
        
        return self.IDEN

class Human(Player):
    
    def getMove(self):
        
        move = int(input("Player "+ self.symbol + ", What is your next move? Enter a number from 1 to 8")) - 1
        
        return move

class Bot(Player):
    
    def getMove(self):
        
        
    
    
    
    
        
        
        
        