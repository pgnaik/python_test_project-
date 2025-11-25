import unittest
from atm import ATM, InsufficientBalanceError, InvalidInputError

class TestATM(unittest.TestCase):

    def test_successful_withdraw(self):
        atm = ATM(1000)
        atm.withdraw(500)
        self.assertEqual(atm.balance, 500)

    def test_insufficient_balance(self):
        atm = ATM(1000)
        with self.assertRaises(InsufficientBalanceError):
            atm.withdraw(1500)

    def test_invalid_negative_amount(self):
        atm = ATM(1000)
        with self.assertRaises(InvalidInputError):
            atm.withdraw(-100)

    def test_invalid_string_amount(self):
        atm = ATM(1000)
        with self.assertRaises(InvalidInputError):
            atm.withdraw("abc")

if __name__ == "__main__":
    unittest.main()
