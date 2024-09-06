
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
    a = int(a)
    b = int(b)
    product = 0
    while a > 0 and b > 0:
        product = product + (a % 10) * (b % 10)
        a = a // 10
        b = b // 10
    return
