
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

    product = a
    a_str = str(a)
    b_str = str(b)
    a_digits = list(a_str)
    b_digits = list(b_str)
    for digit in a_digits:
        product *= int(digit)
    for digit in b_digits:
        product *= int(digit)
    return product
