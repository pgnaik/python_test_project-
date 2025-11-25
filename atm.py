# atm.py
class InsufficientBalanceError(Exception):
    def __init__(self, message="Insufficient balance"):
        self.message = message
        super().__init__(self.message)

class InvalidInputError(Exception):
    pass

class ATM:
    def __init__(self, balance=1000):
        self.balance = balance

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise InvalidInputError("Invalid withdrawal amount")
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient balance. Cannot withdraw amount.")
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")
        except ValueError:
            raise InvalidInputError("Invalid input. Please enter a valid amount.")

    def clone(self):
        return ATM(self.balance)

if __name__ == "__main__":
    # Test cases (manual run)
    try:
        atm = ATM()
        atm.withdraw(500)      # Withdrawal successful
        # atm.withdraw("abc")  # Invalid input
        # atm.withdraw(-100)   # Invalid withdrawal amount
        atm.withdraw(1500)     # Insufficient balance
    except (InsufficientBalanceError, InvalidInputError) as e:
        print(e)

