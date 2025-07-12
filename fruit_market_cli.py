# Fruit Market CLI Program

# Initial fruit data
fruit_list = {
    0: {"name": "Apple", "stock": 20, "price": 10000},
    1: {"name": "Orange", "stock": 15, "price": 15000},
    2: {"name": "Grape", "stock": 25, "price": 20000}
}

next_index = 3  # Next available index for new fruits

while True:
    print("\nWelcome to the Fruit Market\n")
    print("Menu Options:")
    print("1. Show Fruit List")
    print("2. Add New Fruit")
    print("3. Delete Fruit")
    print("4. Buy Fruit")
    print("5. Exit Program")

    menu = int(input("Enter the menu number you want to run: "))

    if menu == 1:
        print("\nFruit List\n")
        print("Index | Name     | Stock | Price")
        for index in fruit_list:
            fruit = fruit_list[index]
            print(f"{index:<5} | {fruit['name']:<8} | {fruit['stock']:<5} | {fruit['price']:<6}")

    elif menu == 2:
        name_new = input("Enter fruit name: ")
        stock_new = int(input("Enter fruit stock: "))
        price_new = int(input("Enter fruit price: "))
        fruit_list[next_index] = {"name": name_new, "stock": stock_new, "price": price_new}
        next_index += 1

        print("Fruit successfully added!")

    elif menu == 3:
        print("\nFruit List\n")
        print("Index | Name     | Stock | Price")
        for index in fruit_list:
            fruit = fruit_list[index]
            print(f"{index:<5} | {fruit['name']:<8} | {fruit['stock']:<5} | {fruit['price']:<6}")

        delete_index = int(input("Enter the index of the fruit you want to delete: "))
        if delete_index in fruit_list:
            del fruit_list[delete_index]
            print("Fruit successfully deleted!")
        else:
            print("Invalid index.")

    elif menu == 4:
        cart = []
        while True:
            print("\nFruit List\n")
            print("Index | Name     | Stock | Price")
            for index in fruit_list:
                fruit = fruit_list[index]
                print(f"{index:<5} | {fruit['name']:<8} | {fruit['stock']:<5} | {fruit['price']:<6}")

            buy_index = int(input("Enter the index of the fruit you want to buy: "))
            if buy_index not in fruit_list:
                print("Invalid index.")
                continue

            qty = int(input("Enter quantity to buy: "))
            if qty > fruit_list[buy_index]["stock"]:
                print(f"Not enough stock, {fruit_list[buy_index]['name']} only has {fruit_list[buy_index]['stock']} left.")
            else:
                fruit_list[buy_index]["stock"] -= qty
                cart.append({
                    "name": fruit_list[buy_index]["name"],
                    "qty": qty,
                    "price": fruit_list[buy_index]["price"]
                })

            continue_buying = input("Do you want to buy another fruit? (yes/no): ").lower()
            if continue_buying != "yes":
                break

        # Display final shopping cart
        print("\nShopping Cart:")
        print("Name     | Qty | Price   | Total")
        total_payment = 0
        for item in cart:
            total = item["qty"] * item["price"]
            total_payment += total
            print(f"{item['name']:<8} | {item['qty']:<3} | {item['price']:<7} | {total}")

        print(f"Total amount to pay: {total_payment}")

        while True:
            amount_paid = int(input("Enter amount of money: "))
            if amount_paid < total_payment:
                print("Insufficient funds. Please enter a sufficient amount.")
            else:
                change = amount_paid - total_payment
                print(f"Your change: {change}")
                print("Thank you for shopping!")
                break

    elif menu == 5:
        print("Thank you for visiting the Fruit Market!")
        break

    else:
        print("Invalid menu option. Please select menu 1-5.")