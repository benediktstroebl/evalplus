
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
    digits = []
    if a != 0:
        while a != 0:
            digits.append(a % 10)
            a //= 10
    if b != 0:
        while b != 0:
            digits.append(b % 10)
            b //= 10
    total = 1
    for digit in digits:
        total *= digit
    if a < 0:
        total *= -1
    return total
