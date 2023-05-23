import math

# Product catalog
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount rules
discount_rules = {
    "flat_10_discount": (200, 10),
    "bulk_5_discount": (10, 0.05),
    "bulk_10_discount": (20, 0.1),
    "tiered_50_discount": (30, 0.5)
}

# Fees
gift_wrap_fee = 1
shipping_fee = 5

# Function to calculate the total cost
def calculate_total_cost(products, gift_wrapping):
    total_quantity = sum(products.values())
    total_cost = 0

    # Apply discount rules
    applicable_discounts = []
    for rule, (threshold, discount) in discount_rules.items():
        if total_quantity > threshold:
            applicable_discounts.append((rule, discount))
    if applicable_discounts:
        applicable_discounts.sort(key=lambda x: x[1], reverse=True)
        discount_rule, discount = applicable_discounts[0]
        total_cost -= math.floor(discount * total_cost)

    # Calculate cost for each product
    for product, quantity in products.items():
        if quantity > 0:
            cost = catalog[product] * quantity

            # Apply gift wrap fee
            if gift_wrapping:
                cost += gift_wrap_fee * quantity

            # Apply discount rule for individual product quantity
            if quantity > discount_rules["bulk_5_discount"][0]:
                cost -= math.floor(discount_rules["bulk_5_discount"][1] * cost)

            total_cost += cost

    # Apply shipping fee
    total_cost += math.ceil(total_quantity / 10) * shipping_fee

    return total_cost

# Get quantity and gift wrap information for each product
products = {}
for product in catalog.keys():
    quantity = int(input(f"Enter quantity for {product}: "))
    gift_wrapping = input(f"Is {product} gift wrapped? (y/n): ").lower() == "y"
    products[product] = quantity

# Calculate and display the total cost
total_cost = calculate_total_cost(products, gift_wrapping)
print("Total cost:", total_cost)