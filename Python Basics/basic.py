
class Bank :
    totalAccount =0;
    def __init__(self,name,amount):
        self.ownerName=name;
        self.amount = amount
        Bank.totalAccount += 1;
    def checkAmount(self):
        return print(f"Your total amount is : {self.amount}")
    @classmethod
    def totalUser (cls):
        return print(f"Total Bank user : {cls.totalAccount}")

    
newUser = Bank("satya",5000);
newUser2 = Bank("Abhi",5000);
newUser.checkAmount()
Bank.totalUser();
newUser2.checkAmount()


