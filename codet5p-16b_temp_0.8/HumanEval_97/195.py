
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
    if a < 0 and b < 0:
        a, b = -a, -b
    for digit in str(a):
        if digit!= '0':
            product += int(digit)
    for digit in str(b):
        if digit!= '0':
            product *= int(digit)
    return product

