# Constants for pizza and topping prices
LARGE_PIZZA_COST = 6.00
EXTRA_LARGE_PIZZA_COST = 10.00
TOPPING_PRICES = {1: 1.00, 2: 1.75, 3: 2.50, 4: 3.35}
HST_RATE = 0.13  # 13% HST

# Get pizza size choice from user
pizza_size = input("Enter the pizza size (Large or Extra Large): ").strip().lower()

# Validate pizza size input
if pizza_size == "large":
    pizza_cost = LARGE_PIZZA_COST
elif pizza_size == "extra large":
    pizza_cost = EXTRA_LARGE_PIZZA_COST
else:
    print("Invalid pizza size entered. Please enter either 'Large' or 'Extra Large'.")
    exit()

# Get number of toppings choice from user
try:
    num_toppings = int(input("Enter the number of toppings (1, 2, 3, or 4): "))
    if num_toppings not in TOPPING_PRICES:
        raise ValueError("Invalid number of toppings.")
except ValueError as e:
    print(e)
    exit()

# Calculate costs
topping_cost = TOPPING_PRICES[num_toppings]
subtotal = pizza_cost + topping_cost
tax = subtotal * HST_RATE
total = subtotal + tax

# Display the subtotal, tax, and total cost
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Tax (HST 13%): ${tax:.2f}")
print(f"Total Cost: ${total:.2f}")
