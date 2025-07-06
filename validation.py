class Validation:

    @staticmethod
    def validate_name(name:str):
        if not isinstance(name, str):
            raise TypeError('Product name must be a string')
        if not name:
            raise ValueError('Product name cannot be empty')


    @staticmethod
    def validate_price(price):
        if not isinstance(price, (float, int)):
            raise ValueError('Product price must be a float')

        if price < 0.0:
            raise ValueError('Product price cannot be negative or zero')


    @staticmethod
    def validate_quantity(quantity):
        if not isinstance(quantity, int):
            raise ValueError('Product quantity must be a int')

        if quantity < 0:
            raise ValueError('Product quantity cannot be negative or zero')


    @staticmethod
    def validate_quantity_available(available_quantity:int, requested_quantity:int):
        if requested_quantity > available_quantity:
            raise ValueError('Requested quantity cannot be greater than available quantity')








