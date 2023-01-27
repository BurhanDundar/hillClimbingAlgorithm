import random
import copy
import time


class board:
    def __init__(self, list=None):
        if list == None:
                self.board = [random.randint(0,8) for i in range(0,8)] # vezirler rastgele dizilmiş şekilde vezirler oluşturuluyor


class queens:
    def __init__(self, numOfRuns, passedboard=None):
        self.totalRuns = numOfRuns
        self.totalSuccess = 0
        for i in range(0, numOfRuns):
            self.totalNumOfSteps = 0
            self.startTime = time.time()
            self.solutionFound = False 
            self.processTime = 0
            self.randomRestartCount = 0
            self.board = board(passedboard)
            self.cost = self.calculateCost(self.board)
            self.hill_solution()
            self.processTime = time.time() - self.startTime
            self.printResults()

    def hill_solution(self):
        while 1:
            currentCost = self.cost
            self.bestNeighbour()
            if currentCost == self.cost:
                if currentCost != 0: # o anki maliyet ("h" değeri) eğer daha iyiye gidemiyorsa random restart çağrılır ve konumun takıldığı local maximumdan çıkması sağlanır
                    self.randomRestartCount += 1
                    self.randomRestart()
                break
            self.totalNumOfSteps += 1
        if self.cost != 0:
            self.totalSuccess += 0
            self.solutionFound = False
        else:
            self.solutionFound = True
            self.totalSuccess += 1
        return self.cost

    def printResults(self): # istenen verileri çıkartma
        print("| ",self.totalNumOfSteps,"\t\t","| ",self.randomRestartCount,"\t\t "," | ","{:.10f}".format(self.processTime),"| ")
        

    def calculateCost(self, tboard): # tahtada bulunan vezirlerin birbirini yeme sayısı (hill climbing konusunda "h" olarak geçmektedir)
        cost = 0
        if len(tboard.board) == 8:
            for i in range(8):
                for j in range(i+1,8):
                    if (tboard.board[i] == tboard.board[j]) or ((j - i) == abs(tboard.board[j] - tboard.board[i])):
                        cost += 1
        return cost

    def bestNeighbour(self): # belli bir kolonu satır satır gezerek en iyi maliyet değerinin o kolon özelinde bulunması
        lowcost = self.calculateCost(self.board)
        bestBoard = self.board
        for i in range (0,8):
            for j in range (0,8):
                if(j != self.board.board[i]):
                    temp = copy.deepcopy(self.board)
                    temp.board[i] = j
                    tempCost = self.calculateCost(temp)
                    if tempCost < lowcost:
                        lowcost = tempCost
                        bestBoard = temp
        self.board = bestBoard
        self.cost = lowcost

    def randomRestart(self): # local maximumda takılan tahtayı yeniden başlatan fonksiyon
        self.board = board(None) # vezirlerin rastgele dağıldığı bir tahta oluştur
        self.cost = self.calculateCost(self.board) # oluşturulan tahtanın maliyetini ("h" değerini) bul
        self.hill_solution()


if __name__ == "__main__": # istenen 16x3 'lük tablonun oluşturulması
    print("8 Queens Random Restart Hill Climbing Solution")
    print(52 * "-")
    print("| Replace Number |"," Random Restart |"," Process Time |")
    print(52 * "-")
    mboard = queens(numOfRuns=15)
    print(52 * "-")