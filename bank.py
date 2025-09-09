import random

class Bank:
    total_banks=0 
    
    def __init__(self, bank_name:str, bank_type:str, bank_branches:str="Abuja") -> None:
        self.bank_name:str=bank_name.capitalize()
        self.bank_type:str=bank_type
        self.bank_total_customers:int=0
        self.bank_branches:list[str]=[bank_branches.capitalize()]
        self.bank_all_accounts:list[str]=[]
        self.bank_all_transactions:list[str]=[]

class Account(Bank):
    def __init__(self, bank: Bank, acc_name:str, acc_type:str, acc_balance:float) -> None: 
        Bank.__init__(self, bank.bank_name, bank.bank_type, bank.bank_branches[0])
        self.acc_name=acc_name
        self.acc_type=acc_type
        self.acc_account_number=random.randint(100, 900)
        self.acc_balance=acc_balance
        self.transaction_count=0
        self.transactions=[]




bank1=Bank("Zenith Bank", "Commercial", "Jos")
# print(first_b.bank_branches.append("Abuja"))
# print(first_b.__dict__)
mp = Account(bank1, "Mp", "savings", 1000)
print(mp.bank_type)
print(mp.bank_name)
print(mp.bank_total_customers)


        
