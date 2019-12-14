class Calculator :
    
    def __init__(self, list) :
        self.list = list
        
    def sum(self) :
        total = 0
        for n in self.list :
            total += n
        return total
    
    def avg(self) :
        total = 0
        for n in self.list :
            total += n
        return total / len(self.list)