
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
    # Do the work
    prod = 0
    while a > 0 and b > 0:
        if a % 10 == b % 10:
            prod = (prod * 10) + (a % 10) + (b % 10)
            a //= 10
            b //= 10
        else:
            a, b = b, a
    return prod
