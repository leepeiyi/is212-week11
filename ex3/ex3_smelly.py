class Product:
    def __init__(self, name, price, discount_rate, tax_rate, item_type):
        self.name = name
        self.price = price
        self.discount_rate = discount_rate
        self.tax_rate = tax_rate
        self.item_type = item_type

    def apply_discount(self):
        discounted_price = self.price - (self.price * self.discount_rate)
        print(f"Discounted price for {self.name} ({self.item_type}): {discounted_price}")
        return discounted_price

    def calculate_tax(self):
        tax = self.price * self.tax_rate
        print(f"Tax for {self.name} ({self.item_type}): {tax}")
        return tax

class Electronics(Product):
    def __init__(self, name, price):
        super().__init__(name, price, discount_rate=0.10, tax_rate=0.15, item_type="Electronics")

class Clothing(Product):
    def __init__(self, name, price):
        super().__init__(name, price, discount_rate=0.20, tax_rate=0.08, item_type="Clothing")

class Grocery(Product):
    def __init__(self, name, price):
        super().__init__(name, price, discount_rate=0.05, tax_rate=0.02, item_type="Grocery")
