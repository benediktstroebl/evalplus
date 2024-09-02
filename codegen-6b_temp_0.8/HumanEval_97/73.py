
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
    res = 0
    for i in range((a // 10), (b // 10) + 1):
        a_d = a % 10
        b_d = b % 10
        res += a_d * b_d
        a //= 10
        b //= 10

    return res
