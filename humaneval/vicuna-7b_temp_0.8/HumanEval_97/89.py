
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
    a_str = str(a)
    b_str = str(b)
    num = 0
    for c in a_str:
        num = num * 10 + int(c)
    for c in b_str:
        num = num * 10 + int(c)
    return num
