
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
    if not 0 <= a < 9 or not 0 <= b < 9:
        raise ValueError("Input must be a two-digit integer.")
    if a == 0 or b == 0:
        return 0
    return int(sum(str(d) * 10 ** (len(str(d))) for d in (a, b)))
