
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

    if not a > 0 or not b > 0:
        return 0
    else:
        return sum(int(x) for x in str(a) if int(x)!= 0) * sum(int(x) for x in str(b) if int(x)!= 0)
