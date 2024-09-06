
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

    product = a * b
    unit_digit_a = str(product)[-1]
    unit_digit_b = str(product)[-2]

    return int(unit_digit_a) * int(unit_digit_b)
