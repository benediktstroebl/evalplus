
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
    a = abs(a)
    b = abs(b)
    res = 0
    while a > 0:
        digit = a % 10
        a = a // 10
        res = res * 10 + digit * b
    while res > 9:
        res = res - (res % 10) + (res // 10)
    return res
