
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
    if isinstance(a, int) and isinstance(b, int):
        res = 0
        for index, digit in enumerate(str(abs(a))):
            res += int(digit) * b
        return res
    else:
        raise ValueError("One of the inputs is not an integer.")

