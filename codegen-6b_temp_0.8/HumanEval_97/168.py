
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
    negative = (a < 0) ^ (b < 0)
    a = -a if negative else a
    b = -b if negative else b
    product = 0
    while a and b:
        digit = a % 10 * b % 10
        product = product * 10 + digit
        a //= 10
        b //= 10
    if a:
        product = product * 10 + a
    if negative:
        product = -product
    return product
