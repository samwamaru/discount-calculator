def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

# Prompting the user for input
original_price_input = input("Enter the original price of the item: ")
discount_percent_input = input("Enter the discount percentage: ")

if original_price_input.isdigit() and discount_percent_input.isdigit():
    original_price = float(original_price_input)
    discount_percent = float(discount_percent_input)
    
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)
    
    # Printing the final price
    if final_price != original_price:
        print("Final price after applying the discount: ${:.2f}".format(final_price))
    else:
        print("No discount applied. Original price: ${:.2f}".format(final_price))
else:
    print("Invalid input. Please enter numeric values for price and discount percentage.")






