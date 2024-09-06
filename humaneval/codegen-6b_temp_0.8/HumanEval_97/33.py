
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
    # return a*b if a > b else b*a
    a, b = abs(a), abs(b)
    product = 0
    for i in range(a):
        product = product * 10 + b
    return product
