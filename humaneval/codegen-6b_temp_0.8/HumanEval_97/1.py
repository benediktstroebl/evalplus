
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
    result = 0
    args = (a, b)
    unit_digit_multiplier = 1
    while args:
        a, b = args
        result += a*unit_digit_multiplier
        args = [b % 10, a % 10]
        args = divmod(args[1], 10)
        unit_digit_multiplier *= 10
    return result
