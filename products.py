class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")


class Electronics(Product):
    def __init__(self, name, price, brand, warranty_months):
        super().__init__(name, price)
        self.brand = brand
        self.warranty_months = warranty_months

    def display(self):
        super().display()
        print(f"Brand: {self.brand}")
        print(f"Warranty: {self.warranty_months} months")


class Clothing(Product):
    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material

    def display(self):
        super().display()
        print(f"Size: {self.size}")
        print(f"Material: {self.material}")


# Example usage
if __name__ == "__main__":
    laptop = Electronics("Laptop", 999.99, "TechCorp", 24)
    shirt = Clothing("T-Shirt", 29.99, "M", "Cotton")

    print("--- Electronics ---")
    laptop.display()

    print("\n--- Clothing ---")
    shirt.display()