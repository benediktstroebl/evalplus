
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
    # Get the unit digits of a and b
    digit_a = str(a)[-1]
    digit_b = str(b)[-1]
    
    # If the last digit of a or b is zero, then the product is 0
    if digit_a == '0' or digit_b == '0':
        return '0'
    
    # If the last digit of a or b is one, then the product is the sum of the digits
    if digit_a == '1' or digit_b == '1':
        return digit_a + digit_b
    
    # If the last digit of a is different from the last digit of b, then the product is the sum of the digits
    if digit_a != digit_b:
        return str(int(digit_a) + int(digit_b))
    
    # If the last digit of a is the same as the last digit of b, then the product is the product of the last digits
    return str(int(digit_a) * int(digit_b))
