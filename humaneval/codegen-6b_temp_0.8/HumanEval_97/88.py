
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
    sign = -1 if a < 0 else 1
    a = abs(a)
    b = abs(b)
    product = 0
    for i in range(a):
        product = product_of_digits(b, product)
    return sign * product

