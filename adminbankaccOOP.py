class WrongPassword(Exception):
    def __init__(self,message):
        super().__init__(message)
class AdminAccessAuthorizationDenied(Exception):
    def __init__(self,message):
        super().__init__(message)
class BankAccount:
    admin_password="12345"
    def __init__(self,password,balance):
        self.balance=balance
        self.__password=password
    def check_balance(self,password):
        if self.__password==password:
            print(f"Current Balance is: {self.balance}")
        else:
            raise WrongPassword("Chutiye password galat hai tera!!")
    def deposit(self,password,amount):
        if self.__password==password:
            self.balance+=amount
            print(f"new balance is: {self.balance}")
        else:
            raise WrongPassword("Chutiye password galat hai tera!!")
    def withdraw(self,password,amount):
        if self.__password==password:
            self.balance-=amount
            print(f"new balance after withdrawl is: {self.balance}")
        else:
            raise WrongPassword("Chutiye password galat hai tera!!")
    def get_password(self):
            return self.__password
    def set_password(self,password,admin):
        if self.admin_password==admin:
            self.__password=password
        else:
            raise AdminAccessAuthorizationDenied("PAssword is wrong")
account=BankAccount("@123",20000)
account.set_password("@@123","12345")
account.check_balance("@@123")