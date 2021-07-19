class ATM(object):
    def __init__(self,name,cardnumber,cardpin):
        self.name=name
        self.cardnumber=cardnumber
        self.cardpin=cardpin
        self.balance=100

    def getName(self):
        return self.name

    def getCardNumber(self):
        return self.cardnumber

    def getCardPin(self):
        return self.cardpin

    def CashWithdrawl(self):
       a=int(input("How much do you want withdraw: "))
       if(a>self.balance):
           print("There is no enough balance to withdraw cash")
       else:
           self.balance=self.balance-a;

    def BalanceEnquiry(self):
        print(self.balance)


pin=int(input("Enter the pin: "))

holder1=ATM("Larry",0000000000000000,pin)
#holder2=ATM("Sergey",9999999999999999,4321)

#print(holder1.getName())
##print(holder2.getName())

opt=int(input("Enter 1 for(CashWithDrawl) or 2 for(BalanceEnquiry)"))

if(opt==1):
    holder1.CashWithdrawl()

if(opt==2):
    holder1.BalanceEnquiry()
