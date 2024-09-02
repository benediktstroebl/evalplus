
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
    a, b = map(int, [a, b])
    while a >= 10000000000000000000 and b >= 100000000000000000000:
        a, b = b, a % 10
    result = 0
    while a > 0:
        result = (result * 10 + (a % 10)) // 10
        a = a // 10
    return result
