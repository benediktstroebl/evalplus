
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
    product = int()
    # multiply = a * b
    # return multiply
    while b > 0:
        digit_add = a + b
        digit_remainder = digit_add % 10
        product = product * 10 + digit_remainder
        b = b / 10

    return product
