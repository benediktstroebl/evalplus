
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
    result = 1
    a = str(a)
    b = str(b)
    for i in range(len(a)):
        result *= int(a[i])
    for i in range(len(b)):
        result *= int(b[i])
    return result
