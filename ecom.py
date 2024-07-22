import tkinter as tk
from tkinter import messagebox

class ShoppingCart:
    def __init__(self, root):
        self.root = root
        self.root.title("PINNACLE's Ecommerce Shopping Cart")
        self.root.configure(bg='lightgrey')  # Set background color for the main window
        
        self.cart = []
        self.item_prices = {}

        # Heading
        self.heading_label = tk.Label(self.root, text="PINNACLE's Ecommerce Shopping Cart", font=('Arial', 16, 'bold'), bg='lightgrey')
        self.heading_label.pack(padx=10, pady=10)

        # Product listing
        self.product_list = tk.Listbox(self.root, width=40)
        self.product_list.pack(padx=10, pady=10)

        # Add products to the list
        self.add_product("Shoes", 10.99)
        self.add_product("Shirts", 9.99)
        self.add_product("Pants", 12.99)
        self.add_product("T-shirts", 7.38)
        self.add_product("Track Pants", 8.79)
        self.add_product("Rain Coat", 15.89)
        self.add_product("Bag", 11.47)
        self.add_product("Watch", 14.26)
        self.add_product("Smart Phone", 20.63)

        # Shopping cart
        self.cart_label = tk.Label(self.root, text="Shopping Cart:")
        self.cart_label.pack(padx=10, pady=10)

        self.cart_list = tk.Listbox(self.root, width=40)
        self.cart_list.pack(padx=10, pady=10)

        # Buttons with custom colors
        self.add_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart, bg='green', fg='white')
        self.add_button.pack(padx=10, pady=10)

        self.remove_button = tk.Button(self.root, text="Remove from Cart", command=self.remove_from_cart, bg='red', fg='white')
        self.remove_button.pack(padx=10, pady=10)

        self.checkout_button = tk.Button(self.root, text="Checkout", command=self.checkout, bg='blue', fg='white')
        self.checkout_button.pack(padx=10, pady=10)

    def add_product(self, product, price):
        self.product_list.insert(tk.END, f"{product} - ${price:.2f}")
        self.item_prices[product] = price

    def add_to_cart(self):
        selected_product = self.product_list.get(tk.ACTIVE)
        if selected_product:
            product, price = selected_product.split(" - $")
            price = float(price)
            self.cart.append((product, price))
            self.cart_list.insert(tk.END, f"{product} - ${price:.2f}")

    def remove_from_cart(self):
        selected_product = self.cart_list.get(tk.ACTIVE)
        if selected_product:
            product, price = selected_product.split(" - $")
            price = float(price)
            self.cart.remove((product, price))
            self.cart_list.delete(tk.ACTIVE)

    def checkout(self):
        total_price = sum([price for _, price in self.cart])
        messagebox.showinfo("Checkout", f"Total price: ${total_price:.2f}")
        # Secure payment processing code goes here

root = tk.Tk()
shopping_cart = ShoppingCart(root)
root.mainloop()
