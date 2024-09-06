
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
    while a > 0 or b > 0:
        digit = a % 10
        a = a // 10
        digit *= b
        b = b // 10
        product = product + digit
    return product
