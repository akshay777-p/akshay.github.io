# Catalog of products with their prices
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount Rules
discount_rules = {
    "flat_10_discount": 10,
    "bulk_5_discount": 5,
    "bulk_10_discount": 10,
    "tiered_50_discount": 50
}

# Fees
gift_wrap_fee = 1
shipping_fee_per_package = 5
units_per_package = 10

# Function to calculate the discount amount
def calculate_discount(cart_total, quantities):
    discount_amount = 0

    if cart_total > 200:
        discount_amount = min(discount_rules["flat_10_discount"], cart_total)

    for product, quantity in quantities.items():
        if quantity > 10:
            product_price = catalog[product]
            item_discount = product_price * quantity * (discount_rules["bulk_5_discount"] / 100)
            discount_amount = max(discount_amount, item_discount)

    total_quantity = sum(quantities.values())
    if total_quantity > 20:
        cart_discount = cart_total * (discount_rules["bulk_10_discount"] / 100)
        discount_amount = max(discount_amount, cart_discount)

    if total_quantity > 30 and any(quantity > 15 for quantity in quantities.values()):
        additional_discount = 0
        for product, quantity in quantities.items():
            if quantity > 15:
                product_price = catalog[product]
                item_discount = (quantity - 15) * product_price * (discount_rules["tiered_50_discount"] / 100)
                additional_discount = max(additional_discount, item_discount)
        discount_amount = max(discount_amount, additional_discount)

    return discount_amount

# Function to calculate the shipping fee
def calculate_shipping_fee(total_quantity):
    package_count = (total_quantity - 1) // units_per_package + 1
    return package_count * shipping_fee_per_package

# Main program
def main():
    quantities = {}

    # Get the quantity for each product
    for product in catalog:
        quantity = int(input(f"Enter the quantity of {product}: "))
        quantities[product] = quantity

    # Calculate and display the details without gift wrapping
    print("Product Details (Without Gift Wrapping):")
    print("--------------------------------------")
    subtotal = 0
    for product, quantity in quantities.items():
        price = catalog[product]
        total_amount = price * quantity
        print(f"{product}: Quantity: {quantity}, Total Amount: ${total_amount}")
        subtotal += total_amount

    discount_amount = calculate_discount(subtotal, quantities)
    shipping_fee = calculate_shipping_fee(sum(quantities.values()))
    total_without_wrapping = subtotal - discount_amount + shipping_fee

    print("--------------------------------------")
    print("Subtotal: $", subtotal)
    if discount_amount > 0:
        print("Discount Applied: Most beneficial discount applied, Amount: $", discount_amount)
    print("Shipping Fee: $", shipping_fee)
    print("Total (Without Gift Wrapping): $", total_without_wrapping)

    # Calculate and display the details with gift wrapping
    print("\nProduct Details (With Gift Wrapping):")
    print("-----------------------------------")
    subtotal_with_wrapping = subtotal + sum(quantities.values()) * gift_wrap_fee
    total_with_wrapping = subtotal_with_wrapping - discount_amount + shipping_fee

    for product, quantity in quantities.items():
        price = catalog[product]
        total_amount = price * quantity
        print(f"{product}: Quantity: {quantity}, Total Amount: ${total_amount}")

    print("-----------------------------------")
    print("Subtotal (With Gift Wrapping): $", subtotal_with_wrapping)
    if discount_amount > 0:
        print("Discount Applied: Most beneficial discount applied, Amount: $", discount_amount)
    print("Shipping Fee: $", shipping_fee)
    print("Gift Wrap Fee: $", sum(quantities.values()) * gift_wrap_fee)
    print("Total (With Gift Wrapping): $", total_with_wrapping)

# Run the program
if __name__ == "__main__":
    main()
