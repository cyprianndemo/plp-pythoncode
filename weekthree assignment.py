def calculate_discount(price, discount_percent):
    """Calculate final price after applying discount if it's 20% or more."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price  # No discount applied

# Get user input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and display final price
final_price = calculate_discount(price, discount_percent)
print(f"Final price: KSH {final_price:.2f}")
