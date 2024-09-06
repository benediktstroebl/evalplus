
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    # Extract the unit digits
    unit_a = a // 100
    unit_b = b // 100
    
    # Add the remaining digits
    remainder_a = a % 100
    remainder_b = b % 100
    
    # Multiply the unit digits
    product_unit = unit_a * unit_b
    
    # Combine the unit and remaining digits
    product = remainder_a + remainder_b
    
    return product_unit * 100 + product
