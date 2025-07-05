class Validation:
    @staticmethod
    def validate_name(name:str):
        if not name:
            raise ValueError('Name cannot be empty')

    @staticmethod
    def validate_price(price:float):
        if price < 0:
            raise ValueError('Price cannot be negative or zero')

    @staticmethod
    def validate_quantity(quantity:int):
        if quantity < 0:
            raise ValueError('Quantity cannot be negative or zero')

    @staticmethod
    def validate_quantity_available(available_quantity:int, requested_quantity:int):
        if requested_quantity > available_quantity:
            raise ValueError('Requested quantity cannot be greater than available quantity')





