def multiply(a, b):
    # Extract the unit digit of the first number
    dig1 = a % 10
    
    # Extract the unit digit of the second number
    dig2 = b % 10
    
    # Multiply the unit digits
    product = dig1 * dig2
    
    # If the product is greater than 9, it will be a decimal number, so we set it to 0
    # to ensure the result is a whole number
    if product > 9:
        product = 0
    
    # Return the final product of unit digits
    return product