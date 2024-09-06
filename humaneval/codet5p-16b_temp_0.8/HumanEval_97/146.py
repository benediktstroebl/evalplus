
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

    prod = 0
    a_digits = [int(c) for c in str(a) if c.isdigit()]
    b_digits = [int(c) for c in str(b) if c.isdigit()]
    for digit in a_digits:
        prod += digit * b_digits[a_digits.index(digit)]
    return prod

