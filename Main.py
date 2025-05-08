class BankAccount


def __init__(self, account_number, account_holder, balance = 0.0):
  self.account_number = account_number
  self.acount_holder = account_holder
  self.balance = float(balance)

def deposit(self, amount):
  return self.balance = self.balance + amount

def withdraw(self, amount):
  if self.balance <= 0.0:
    print(f'Error insufficient funds! ')
  else
    return self.balance = amount - self.balance
def display_balance(self):
  print(f'Current Balance: {self.balance}')

def__str__(self):
  return f'Account Details: \n  Account Holder: {account_holder}\n Account Number: {account_number}\n Account Balance: {self.balance}'
