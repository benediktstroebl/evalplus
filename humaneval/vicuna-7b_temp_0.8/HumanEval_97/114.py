
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
    # 10, 1, 1, 1, 1, 1, 1, 1, 1
    # 10, 1, 1, 1, 1, 1, 1, 1, 1
    # 0, 0, 0, 0, 0, 0, 0, 0, 0
    # 0, 0, 0, 0, 0, 0, 0, 0, 0
    return (int(a / 100) * int(b / 100)) + (int(a % 100) * int(b % 100)) + \
        (int(a % 10) * int(b % 10)) + (int(a % 1) * int(b % 1))