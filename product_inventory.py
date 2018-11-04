# Create a product class which has a price, id, and quantity on hand. 
# Then create an inventory class which keeps track of various products 
# and can sum up the inventory value.


class Product:
    def __init__(self, name, price, id, quantity):
        self.item_dict = {'name': name, 'price': price, 'id': id,  'quantity': quantity}

    def get_products(self):
        return (self.item_dict['name'], self.item_dict['price'], 
                self.item_dict['id'], self.item_dict['quantity'])

    #Return single product    
    def get_product(self, product):
        return self.item_dict[product]

class Inventory:
    def __init__(self): 
        # Make a list of item dictionaries
        self.products = []

    def set_product(self, name, price, id, quantity):
        product = Product(name, price, id, quantity)
        self.products.append(product)

    #Make unique lists of ID, Price, and Quantity
    def list_products(self):
        for p in self.products:
            name, price, id, quantity = p.get_products()

            print("Product: {} Price: ${} ID: {} Quantity: {}".format(name, price, id, quantity))

    def value(self):
        #list comprehension to calculate the price of the products in the inventory
        values = [product.get_product("price") for product in self.products]
        #formats the total value
        return "Total Value: {}".format(sum(values))
     
# Here we have created an instance of the the Inventory class        
inventory_1 = Inventory()
# Here we have set the products with its name, price, id, and the num of quantity
inventory_1.set_product("Shampoo", 3.42, 1, 3)
inventory_1.set_product("Candy", 5.99, 2, 50)

#print(inventory_1.products.value())

#Listing the products that are already within the inventory
inventory_1.list_products()

#Calculates the total price 
print(inventory_1.value())

      
       