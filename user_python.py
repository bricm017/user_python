class User:
    def __init__(self, name, email_address, account_balance):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def display_user_balance(self):
        print("User: " , self.name, " balance: " , self.account_balance)
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self,amount):
        self.account_balance -= amount
    def transfer_money(self, User, amount):
        self.make_withdrawal(amount)
        User.make_deposit(amount)

Sarah = User("Sarah","sarahnmaze@gmail.com", 0)
Andy = User("Andy","andystoyz@gmail.com", 0)
Zelda = User("Zelda","triforce@gmail.com", 0)
#User 1: making 3 deposits and 2 withdrawals
Sarah.make_deposit(200)
Sarah.make_deposit(2660)
Sarah.make_deposit(500)
Sarah.make_withdrawal(300)
Sarah.display_user_balance()
#User 2: making 2 deposits and 2 withdrawals
Andy.make_deposit(1000)
Andy.make_deposit(50660)
Andy.make_withdrawal(2000)
Andy.make_withdrawal(500)
Andy.display_user_balance()
#User 3: making 1 deposits and 3 withdrawals
Zelda.make_deposit(300000)
Zelda.make_withdrawal(5060)
Zelda.make_withdrawal(57000)
Zelda.make_withdrawal(1000)
Zelda.display_user_balance()

Sarah.transfer_money(Zelda, 350)
Sarah.display_user_balance()
Zelda.display_user_balance()
