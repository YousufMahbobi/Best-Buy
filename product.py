import validation
from validation import Validation

class Product:
    def __init__(self, name, price, quantity):
        Validation.validate_name(name)
        Validation.validate_price(price)
        Validation.validate_quantity(quantity)

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        Validation.validate_quantity(quantity)
        self.quantity += quantity
        self.check_and_deactivate_product_out_of_stock()


    def is_active(self):
        return self.active


    def deactivate(self):
        self.active = False

    def show(self):
        print(f'{self.name}, Price: {self.price}, Quantity: {self.quantity}')

    def buy(self, quantity):
        Validation.validate_quantity(quantity)
        if self.is_active():
            Validation.validate_quantity_available(self.quantity, quantity)
            self.quantity -= quantity
            self.check_and_deactivate_product_out_of_stock()
            return quantity * self.price
        return 0

    def check_and_deactivate_product_out_of_stock(self):
        if self.quantity == 0:
            self.deactivate()



bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())


bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()