
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
    # Initialize product to 0
    product = 0

    # Find the unit digit of the first integer
    unit_digit_a = a % 10

    # Find the unit digit of the second integer
    unit_digit_b = b % 10

    # Multiply the two unit digits
    product = unit_digit_a * unit_digit_b

    return product
