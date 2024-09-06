
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
    # first check for zero
    if a == 0 or b == 0:
        return 0

    # compute the rest of the digits
    rest = 0
    carry = 0
    while abs(a) > 10:
        carry = a // 10
        a = abs(a) - 10
        rest = multiply(a, b) + carry
        a = carry * 10 + abs(a) % 10

    # handle the unit digit
    return rest + multiply(a, b) % 10
