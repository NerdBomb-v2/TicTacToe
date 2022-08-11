class ttt():
    def __init__(self):
        self.table = [1,2,3,4,5,6,7,8,9]
        self.winner = None
        self.move = 0
        self.player = 'x'
        self.opponent = 'o'

    def mark(self,symbol,index)->None:
        try:
            if 9>=index>0 and len(symbol)<=1 and type(self.table[index-1])==int and self.status()==True :
                self.table[index-1] = symbol
                self.move+=1
            else:
                if self.status()==True:
                    print("Only 1 character with valid index is allowed as a symbol.")
                else:
                    print(f"Can't play the winner is {self.winner}")
        except:
            if self.status()==True:
                print("Only 1 character with valid index is allowed as a symbol.")
            else:
                print(f"Can't play the winner is {self.winner}")

    def status(self)->bool:   #returns true when the game is playable
        #checking rows
        if self.table[0]==self.table[1]==self.table[2]:
            self.winner = self.table[0]
            return False
        elif self.table[3]==self.table[4]==self.table[5]:
            self.winner = self.table[3]
            return False
        elif self.table[6]==self.table[7]==self.table[8]:
            self.winner = self.table[6]
            return False

        #checking columns
        elif self.table[0]==self.table[3]==self.table[6]:
            self.winner = self.table[0]
            return False
        elif self.table[1]==self.table[4]==self.table[7]:
            self.winner = self.table[1]
            return False
        elif self.table[2]==self.table[5]==self.table[8]:
            self.winner = self.table[2]
            return False

        #checking diagonals
        elif self.table[0]==self.table[4]==self.table[8]:
            self.winner = self.table[0]
            return False
        elif self.table[2]==self.table[4]==self.table[6]:
            self.winner = self.table[2]
            return False

        else: #If the winner is still noone
            return True
    def isMoveLeft(self):
        for i in range(9):
            if type(self.table[i])==int:
                return True
                break
        else:
            return  False
    def evaluate(self)->int:
        if self.status()==False:
            if self.winner==self.player:
                return 10
            elif self.winner==self.opponent:
                return -10
        else:
            return False

    def minimax(self,depth,isMax): #isMax is True for maximizer
        score = self.evaluate()

        if score==10 or score==-10:
            return score

        if self.isMoveLeft()==False:
            return 0

        if isMax: #player
            best=-1000
            for i in range(9):
                if type(self.table[i])==int:
                    self.table[i]=self.player
                    best = max( best, self.minimax(depth + 1,not isMax) )
                    self.table[i]=i+1
            return best

        else: #opponent
            best =1000
            for i in range(9):
                if type(self.table[i])==int:
                    self.table[i]=self.opponent
                    best = min( best, self.minimax(depth + 1,not isMax) )
                    self.table[i]=i+1
            return best

    def findBestMove(self):
        bestVal=-1000
        bestMove=-1

        for i in range(9):
            if type(self.table[i])==int:
                self.table[i]=self.player
                moveVal = self.minimax(0, False)
                self.table[i]=i+1
                if (moveVal > bestVal) :               
                    bestMove = i
                    bestVal = moveVal
        return bestMove

    def ai_move(self):
        self.mark(self.player,self.findBestMove()+1)
    
    def reset(self):
        self.table = [1,2,3,4,5,6,7,8,9]
        self.winner=None
        self.move=0
        
    def __str__(self):  #returns good looking TTT board
        table=' _________ \n'
        table+=f'| {str(self.table[0]):^1}  {str(self.table[1]):^1}  {str(self.table[2]):>1} |\n'
        table+='|_________|\n'
        table+=f'| {str(self.table[3]):^1}  {str(self.table[4]):^1}  {str(self.table[5]):>1} |\n'
        table+='|_________|\n'
        table+=f'| {str(self.table[6]):^1}  {str(self.table[7]):^1}  {str(self.table[8]):>1} |\n'
        table+='|_________|\n'
        table=table.replace('True','O')
        table=table.replace('False',' X')
        table=table.replace('None','.')

        return table
