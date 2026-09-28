
class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        # Check if coffee is already in the order
        for item in self.items:
            if item["coffee"].name == coffee.name:
                item["quantity"] += 1
                print(f"Added another {coffee.name} to your order.")
                return

        # If coffee is not already in the order
        self.items.append({
            "coffee": coffee,
            "quantity": 1
        })

        print(f"Added {coffee.name} to your order.")

    def total(self):
        total = 0

        for item in self.items:
            total += item["coffee"].price * item["quantity"]

        return total

    def show_order(self):
        if not self.items:
            print("No items in order.")
            return

        print("\nYour Order:")

        for i, item in enumerate(self.items, 1):
            coffee = item["coffee"]
            quantity = item["quantity"]
            item_total = coffee.price * quantity

            print(
                f"{i}. {coffee.name} - "
                f"${coffee.price} x {quantity} = ${item_total}"
            )

        print(f"Total: ${self.total()}\n")

    def checkout(self):
        if not self.items:
            print("Your cart is Empty.")
            return

        self.show_order()

        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()

        if confirm == "yes":
            print("Order confirmed! Thank you.")
            self.items.clear()
        else:
            print("Checkout cancelled.")


def main():
    menu = [
        Coffee("Espresso", 2.5),
        Coffee("Latte", 3.5),
        Coffee("Cappuccino", 3.0),
        Coffee("Americano", 2.0)
    ]

    order = Order()

    while True:
        print("\n--- Coffee Menu ---")

        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price}")

        print("5. View Order")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice in ["1", "2", "3", "4"]:
            order.add_item(menu[int(choice) - 1])

        elif choice == "5":
            order.show_order()

        elif choice == "6":
            order.checkout()

        elif choice == "7":
            print("Thanks for visiting. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()


