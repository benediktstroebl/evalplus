
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
    product = 0
    lastA = 0
    lastB = 0
    if a <= 0:
        lastA = a * -1
    else:
        lastA = a
    if b <= 0:
        lastB = b * -1
    else:
        lastB = b
    product = lastA % 10
    product *= lastB % 10
    return product
