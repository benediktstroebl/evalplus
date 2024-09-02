
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
    if a == 0 or b == 0:
        return 0
    a1 = a % 10
    b1 = b % 10
    # If a is negative, the product of a1 * b1 and b / 10 is the product of a1 * b / 10.
    # If a is positive, the product of a1 * b1 and b1 / 10 is the product of a1 * (b1 / 10) + b
    # For example, if a is -11 (which is -19 in decimal),
    # the product of a1 * b1 and b1 / 10 is the product of (a1 * b1 / 10) + b1 / 10 = (19 / 10) + b1
    # Therefore we do not have to consider negative numbers.
    # if a is negative, we can divide the product by 10 to get the product of a1 * b1, then divide by 10 to get (a1 * b1 / 10) + b1
    # if a is positive, we can multiply the product by 10 to get (a1 * b1 * 10) + b1
    return (a1 * b1) + (b1 * 10) if a > 0 else (a1 * b1) + (b1 / 10)

