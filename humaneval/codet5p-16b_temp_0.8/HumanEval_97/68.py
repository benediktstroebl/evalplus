
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

    if b == 0:
        return 0
    if b > 0:
        a = abs(a)
        b = abs(b)
        total = 0
        while b > 0:
            digit = a % 10
            total += digit * b
            b = b // 10
            a = a // 10
        return total
    if b < 0:
        total = 0
        while a > 0:
            digit = a % 10
            total += digit * b
            b = b // 10
            a = a // 10
        return total

