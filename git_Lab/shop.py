class Product:
    def __init__(self, sku, name, price):
        if not sku:
            raise ValueError("sku is required")
        self.sku = sku
        self.name = name
        self.price = price

def apply_discount(price, percent):
    return price * (100 - percent) / 100

def add_tax(price, rate=0.2):
    return price * (1 + rate)

def apply_coupon(price):
    return price - 5
# TODO half-done