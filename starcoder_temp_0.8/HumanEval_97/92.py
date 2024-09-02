
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

    # make sure the smaller number is the first argument
    if a > b:
        a, b = b, a
    return sum(int(n) for n in str(a)[:2]) * sum(int(n) for n in str(b)[:2])
