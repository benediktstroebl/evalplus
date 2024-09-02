
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
    # Check if the input is negative
    if b < 0:
        # Flip the input
        a, b = b, -a
    # If the input is negative, the result will be negative
    # so we need to add 256 to the result
    result = 0
    while a != 0:
        if (a % 10) == (b % 10):
            result += a // 10
            a, b = b, a % 10
        else:
            result += (a // 10) * (10 - b % 10)
            a, b = b, a // 10
    return result + 256
