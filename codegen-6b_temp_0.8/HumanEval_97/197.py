
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
    def mul_indexes(a, b):
        if b == 0:
            return 0
        if b > 0:
            return 1 + (a * mul_indexes(a, b - 1))
        else:
            return (10 * mul_indexes(a, b + 1))

    if a == 0 or b == 0:
        return 0
    return mul_indexes(a, abs(b))
