
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
    a_digits = get_digits(a)
    b_digits = get_digits(b)
    product = 0
    for a_digit in a_digits:
        for b_digit in b_digits:
            product += a_digit*b_digit
    return product
