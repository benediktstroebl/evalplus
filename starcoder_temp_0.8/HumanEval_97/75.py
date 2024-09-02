
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
    num_1 = abs(a)
    num_2 = abs(b)
    num_1 = str(num_1)
    num_2 = str(num_2)
    return int(num_1[0]) * int(num_2[0])

