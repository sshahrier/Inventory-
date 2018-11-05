# Create a product class which has a price, id, and quantity on hand. 

class Product:
    def __init__(self, name, price, _id, quantity):
        self.item_dict = {'name': name, 'price': price, 'id': _id,  'quantity': quantity}

    def get_products(self):
        return (self.item_dict['name'], self.item_dict['price'], 
                self.item_dict['id'], self.item_dict['quantity'])

    #Return single product    
    def get_product(self, product):
        return self.item_dict[product]
