
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
    a, b = abs(a), abs(b)
    if a > b:
        a, b = b, a
    result = 0
    while a > 0:
        carry, a = a % 10, a // 10
        b = b % 10
        result = result * 10 + carry * b
    return result
