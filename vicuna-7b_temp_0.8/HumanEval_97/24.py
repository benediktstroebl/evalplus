
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
    # Divide the first digit of the second number by the first digit of the first number
    unit_digit_2 = b // a
    
    # If the remainder is greater than 9, the product is negative
    if unit_digit_2 > 9:
        product = -1
    else:
        product = 1
        
    # If the second number has only one digit, return the product with the correct sign
    if len(str(b)) == 1:
        return product * str(b)[-1]
        
    # Multiply the unit digit of the second number by the correct product
    product *= str(a)[0]
    
    # Multiply the remaining digits of the second number by the correct product
    for digit2 in str(b)[1:]:
        product *= str(digit2)
    
    return product