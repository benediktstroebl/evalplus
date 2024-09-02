
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
    # google it to find how to iterate between 0 and the length of the string
    return sum([int(digit) for digit in str(a * b)])
