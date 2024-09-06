
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
    # ...
    if d1 > 9:
        return (d1 - 1) * 10 + d2
    if d2 > 9:
        return (d2 - 1) * 10 + d1
    if d1 == d2 == 0:
        return 10
    return 0
