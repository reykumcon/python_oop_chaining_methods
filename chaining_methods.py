class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"Money transfer from {self.name} to {other_user.name}... \nTransfer Amount: {amount}")
        return self

alice = User('Alice', 'alice@account.com')
ben = User('Ben', 'ben@account.com')
charlie = User('Charlie', 'charlie@account.com')

alice.make_deposit(10).make_deposit(20).make_deposit(30).make_withdrawal(10).display_user_balance()

ben.make_deposit(20).make_deposit(30).make_withdrawal(10).make_withdrawal(10).display_user_balance()

charlie.make_deposit(50).make_withdrawal(10).make_withdrawal(10).make_withdrawal(10).display_user_balance()

alice.transfer_money(charlie, 10).display_user_balance()
charlie.display_user_balance()