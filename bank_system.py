class BankSystem:

    def __init__(self):
        self.accounts={}     #accounts store as dictionary
    
    def create_account(self,name,acc,pin,bal):
        if acc in self.accounts:
            print("Account already exist")
            return
        account=BankAccount(name,acc,pin,bal)

        self.accounts[acc]=account
        print("Account created successfully")
        print()
    
    def get_account(self,acc):
        if acc in self.accounts:
            return self.accounts[acc]
        else:
            print("Account not found")
            return None
        

class BankAccount:
    def __init__(self,name,acc,pin,bal):
        self.name=name
        self._acc=acc
        self.__pin=pin
        self.__bal=float(bal)
        self.transaction=[]  # for transaction history in list
    def deposit(self,amt):
        try:
            if(amt<=0):
                raise ValueError("Amount must be positive")
            else:
                self.__bal+=amt
                self.transaction.append(f"Deposited {amt}")
                print("Amount deposited successfully")
                print()
        except ValueError as e:
            print(e)
            

    def withdraw(self,amt,pin):
        try:
            if pin!=self.__pin:
                raise Exception("Incorrect Pin")
            if amt<=0:
                raise ValueError("Amount must be positive")
            if(amt>self.__bal):
                raise Exception("Insufficient balance")
            self.__bal=self.__bal-amt
            self.transaction.append(f"Withdrawn {amt}")
            print("Successfully withdrawn")
            print()
        except Exception as e:
            print(e)


    def check_bal(self,pin):
        try:
            if self.__pin!=pin:
                raise Exception("Incorrect Pin!")
            print("Current Balance: ",self.__bal)
        except Exception as e:
            print(e)
        

    def transfer(self,receiver,amt,pin):
     try:
        if(receiver._acc == self._acc):
            raise Exception("Cannot transfer to same Account")
        if(pin!=self.__pin):
            raise Exception("Incorrect pin")
        if(amt<=0):
            raise Exception("Amount must be positive")
        if(amt>self.__bal):
            raise Exception("Insufficient balance")
        self.__bal-=amt
        receiver.__bal+=amt

        self.transaction.append(f"Transferred {amt} to {receiver.name}")
        receiver.transaction.append(f"Transferred {amt} from {self.name}")
        print("Transfer successful")
        print()
     except Exception as e:
         print(e)

    def show_trans(self):
        print("Transaction History")
        if len(self.transaction)==0:
            print("No transactions yet")
        else:
            for t in self.transaction:
                print(t)
        print()

    def account_details(self):
        print("Account details:")
        print("Name:",self.name)
        print("Acc no: ",self._acc)
        print("Bal: ",self.__bal)

    def change_pin(self,oldpin,newpin):
        try:
            if oldpin!=self.__pin:
                raise Exception("Incorrect old pin")
            if len(str(newpin)) !=4:
                raise Exception("Pin must be 4 digit")
            self.__pin=newpin
            print("Pin changed successfully")
            print()
        except Exception as e:
            print(e)


# main method

bank=BankSystem()

#menu system

while True:
    print("-----Bank Menu-----")
    print("1 Deposit")
    print("2 Withdraw")
    print("3 Transfer")
    print("4 Show transactions")
    print("5 Account details")
    print("6 Create Account")
    print("7 Check Balance")
    print("8 Change Pin")
    print("9 Exit")

    choice=int(input("Enter choice: "))

    if(choice==1):
        acc=int(input("Enter Account Number:"))
        amt=float(input("Enter amount: "))
        # object to link BankSystem
        account=bank.get_account(acc)
        #check if account exist in the bankSystem
        if account:
            account.deposit(amt)   #means BankAccount.deposit(account, amount)

    elif(choice==2):
        acc=int(input("Enter Acc no: "))
        amt=int(input("Enter amount: "))
        pin=int(input("Enter pin: "))
        account=bank.get_account(acc)
        if account:
            account.withdraw(amt,pin)

    elif(choice==3):
        acc1=int(input("Enter Your Acc no:"))
        acc2=int(input("Enter Receiver Acc no: "))
        amt=int(input("Enter amount: "))
        pin=int(input("Enter pin: "))

        account=bank.get_account(acc1)
        account2=bank.get_account(acc2)

        if(account and account2):
            account.transfer(account2,amt,pin)

    elif(choice==4):
        acc=int(input("Enter acc no: "))
        account=bank.get_account(acc)
        if account:
            account.show_trans()

    elif(choice==5):
        acc=int(input("Enter Account no:"))
        account=bank.get_account(acc)
        if account:
            account.account_details()
   
    elif(choice==6):
        name=input("Enter Account Holder name: ")
        acc=int(input("Enter Acc number: "))
        pin=int(input("Enter 4 digit pin: "))
        bal=float(input("Enter Current Balance: "))

        account=bank.create_account(name,acc,pin,bal)

    elif(choice==7):
        acc=int(input("Enter Acc no: "))
        pin=int(input("Enter your Pin number: "))

        account=bank.get_account(acc)
        if account:
            account.check_bal(pin)

    elif(choice==8):
        acc=int(input("Enter acc no: "))
        pin=int(input("Enter old pin: "))
        newpin=int(input("Enter new pin: "))

        account=bank.get_account(acc)
        if account:
            account.change_pin(pin,newpin)

    elif(choice==9):
        print("Thank You for using the Banking System.")
        break
    else:
        print("Invalid choice.Please try again.")


