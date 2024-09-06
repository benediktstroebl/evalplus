
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
    prod = 0
    a = abs(a)
    b = abs(b)
    while a:
        prod += a%10
        a //= 10
    while b:
        prod += b%10
        b //= 10
    return prod
