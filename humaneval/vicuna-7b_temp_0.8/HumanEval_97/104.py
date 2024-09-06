
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
    # check for negative numbers
    if b < 0:
        return -multiply(a, abs(b))
    # check if the numbers have leading zeroes
    if a < 100 or b < 100:
        return 0
    # pad the number with zeros
    a = str(a)
    b = str(b)
    a = a.rjust(len(b), '0')
    b = b.rjust(len(a), '0')
    return int(a[:len(b)] * int(b))
