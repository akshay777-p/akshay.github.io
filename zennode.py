catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

discount_rules = {
    "flat_10_discount": 10,
    "bulk_5_discount": 5,
    "bulk_10_discount": 10,
    "tiered_50_discount": 50
}

gift_wrap_fee = 1
shipping_fee_per_package = 5
units_per_package = 10

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

def calculate_shipping_fee(total_quantity):
    package_count = (total_quantity - 1) // units_per_package + 1
    return package_count * shipping_fee_per_package

def main():
    quantities = {}
    
    for product in catalog:
        quantity = int(input(f"Enter the quantity of {product}: "))
        quantities[product] = quantity
    
    gift_wrapping = input("Do you want gift wrapping? (yes/no): ").lower() == "yes"
    
    print("Product Details:")
    print("----------------")
    subtotal = 0
    for product, quantity in quantities.items():
        price = catalog[product]
        total_amount = price * quantity
        print(f"{product}: Quantity: {quantity}, Total Amount: ${total_amount}")
        subtotal += total_amount
    
    discount_amount = calculate_discount(subtotal, quantities)
    shipping_fee = calculate_shipping_fee(sum(quantities.values()))
    total = subtotal - discount_amount + gift_wrap_fee * sum(quantities.values()) + shipping_fee
    
    print("----------------")
    print("Subtotal: $", subtotal)
    if discount_amount > 0:
        print("Discount Applied: Most beneficial discount applied, Amount: $", discount_amount)
    print("Shipping Fee: $", shipping_fee)
    print("Gift Wrap Fee: $", gift_wrap_fee * sum(quantities.values()))
    print("Total: $", total)

if __name__ == "__main__":
    main()
