# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

# Create a product class which has a price, id, and quantity on hand. 
# Then create an inventory class which keeps track of various products 
# and can sum up the inventory value.


class Product:
    def __init__(self, name, price, id, quantity):
        self.name = name
        self.price = price
        self.id = id
        self.quantity = quantity
        self.item_dict = {'Name: ': self.name, 'Price: ': self.price, 'ID: ': self.id,  'Quantity: ': self.quantity}

class Inventory:
    def __init__(self, products): 
        # Make a list of item dictionaries
        self.name, self.id, self.price_list, self.quan_list = [], [], [], []
        self.products = [prod_1.item_dict, prod_2.item_dict]
    @property
    def value():
        return sum(product.price for product in self.products)
        
    #Make unique lists of ID, Price, and Quantity
    def list_products(self):
        for i in self.products:
            self.name.append(i['Name: '])
            self.id.append(i['ID: '])
            self.price_list.append(i['Price: '])
            self.quan_list.append(i['Quantity: '])

    #print(sum(self.price_list)) 
        
      
prod_1 = Product(Bob, 1, 23, 4)
prod_2 = Product(John, 2, 24, 3)
    
inventory_1 = Inventory()
        #, product_set, inventory_sum):
        # self.id
      
        #super().__init__(price, id, quantity
                         
          # self.product_set = product_set
          # self.inventory_sum = inventory_sum

        
    #def add_product(name, id, price, quantity):
     #   $name = Product(id, price, quantity)
      #  product_set.append($name)
                         
             
    # def add(self):
      
       
    

 
#Inventory.add_product(coke, 4, 10, 5)
#print(Inventory.add_product(coke, 4, 10, 5))


