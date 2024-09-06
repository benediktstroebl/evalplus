
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
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError
    if a <= 0 or b <= 0:
        raise ValueError
    product = 0
    for i in range(b):
        product = product * 10 + a
    return product

