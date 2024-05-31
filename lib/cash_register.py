class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.item_prices = []  # Maintain a list to store prices of individual items

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.item_prices.extend([price] * quantity)  # Adds individual prices to the list

    def apply_discount(self):
        if self.discount > 0:
            self.total *= (100 - self.discount) / 100
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.item_prices[-1]  # Get the price of the last item
            self.total -= last_item_price
            del self.items[-1]
            del self.item_prices[-1]  # Remove the last item's price
        else:
            print("No transactions to void.")

            #remaining tests
# CashRegister in cash_register.py prints success message with updated total Failed
# CashRegister in cash_register.py reduces the total Failed
# CashRegister in cash_register.py returns the total to 0.0 if all items have been removed Failed