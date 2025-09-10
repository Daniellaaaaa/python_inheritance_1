import random
from enum import Enum

class AccountType(Enum):
    SAVINGS = "savings"
    CURRENT = "current"

class TransactionType(Enum):
    DEBIT = "debit"
    CREDIT = "credit"


class Bank:
    total_banks=0 
    banks_created={}
    
    def __init__(self, bank_name:str, bank_type:str, bank_branches:str="Abuja") -> None:
        self.bank_name:str=bank_name  #capitalize()
        self.bank_type:str=bank_type
        self.bank_total_customers:int=0
        self.bank_branches:list[str]=[bank_branches]  #capitalize
        #self.bank_branches.append(bank_branches)
        self.bank_all_accounts:list[str]=[]
        self.bank_all_transactions:list[str]=[]
        

    def register_bank(self)->str:
        if self.bank_name not in Bank.banks_created:
            Bank.banks_created[self.bank_name]= self.bank_branches
            Bank.total_banks+=1
            return f"{self.bank_name} Created successfully"
        else:
            for branch in self.bank_branches:
                if branch not in Bank.banks_created[self.bank_name]:
                    Bank.banks_created[self.bank_name].append(branch)
                    Bank.total_banks+=1
                else:
                    return "This branch already exist"    
            return f"Branch updated"
        
    def total_customers(self)->str:
        return f"Total number of customers in {self.bank_name}, {self.bank_branches[0]} branch: {self.bank_total_customers}"
        
    def all_accounts(self)->str:
        return f"All acounts for {self.bank_name}: {self.bank_all_accounts}"    
    
    def all_transactions(self)->str:
        return f"All {self.bank_name} Transactions: {self.bank_all_transactions}"
    
    def all_banks_created(self)->str:
        return f"All Banks: {Bank.banks_created}"


    def total_banks_created(self)->str:
        return f"Total banks created are: {Bank.total_banks}"


class Account(Bank):
    def __init__(self, bank: Bank, acc_name:str, acc_type:str, acc_balance:float) -> None: 
        Bank.__init__(self, bank.bank_name, bank.bank_type, bank.bank_branches[0])
        self.bank=bank
        self.acc_name=acc_name
        self.acc_type=acc_type
        self.acc_account_number=random.randint(100, 900)
        self.acc_balance=acc_balance
        self.transaction_count=0
        self.transactions=[]
        each_account={self.acc_name:self.transactions}
        bank.bank_all_transactions.append(each_account)

    def register_account(self)->str:
        self.bank.bank_total_customers+=1
        self.bank.bank_all_accounts.append(self.acc_name)
        return f"{self.acc_name} created successfully, Account Number: {self.acc_account_number}"
    
    def deposit(self, amount):
        if amount<=0:
            return "Invalid amount"
        else:
            self.transactions.append(f"{TransactionType.CREDIT.value}:{amount}")
            self.transaction_count+=1
            self.acc_balance+=amount
            return f"{amount}N received in {self.acc_name} account"
        
    def withdraw(self, amount):
        if amount<=0:
            return "Invalid amount"
        elif amount<=self.acc_balance:
            self.transactions.append(f"{TransactionType.DEBIT.value}:{amount}")
            self.transaction_count+=1
            self.acc_balance-=amount
            return f"{amount}N removed in {self.acc_name} account"    
        else:
            return f"Insufficient balance"


#FOR BANKS
bank1=Bank("Zenith Bank", "Commercial", "Lagos")
bank2=Bank("Zenith Bank", "Commercial", "Jos")
bank3=Bank("Jaiz", "Commercial", "Jos")        

print(bank1.register_bank())
print(bank2.register_bank())
print(bank3.register_bank())

print(bank1.all_banks_created())
print(bank1.total_banks_created())



#FOR ACCOUNTS
mp = Account(bank1, "Mp", AccountType.SAVINGS, 1000)
joy = Account(bank1, "Joy", AccountType.SAVINGS, 1000)

print(joy.register_account())
print(mp.register_account())
print(bank1.total_customers())
print(bank1.all_accounts())

print(mp.deposit(100))
print(joy.deposit(50))
print(mp.transactions)
print(mp.transaction_count)
print(bank1.all_transactions())
print(mp.withdraw(100))
print(joy.withdraw(50))
print(mp.transaction_count)
print(bank1.all_transactions())

print(Bank.banks_created)





# bank1=Bank("Zenith Bank", "Commercial", "Lagos")
# bank3=Bank("Jaiz", "Commercial", "Jos")
# print(first_b.bank_branches.append("Abuja"))
# print(first_b.__dict__)

# print(bank1.bank_branches)
# print(mp.bank_type)
# print(mp.bank_name)
# print(mp.bank_total_customers)

# print(bank1.__dict__)



        
