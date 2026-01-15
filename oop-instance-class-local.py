class House:
    counter = 0
    def __init__(self, address, area, price ):
        self.address = address
        self.area = area
        self.price = price
        House.counter += 1

    def present(self):
        print(f" house is at : {self.address} or area: {self.area} sqft  with price: {self.price} USD ")


house1 = House("123 Main St", 1500, 300000)
house2 = House("456 Oak Ave", 2000, 450000)
house1.present()
house2.present()
print('Houses created:', House.counter)
