
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
    if a == 0 or b == 0:
        return 0
    a = abs(a)
    b = abs(b)

    dict = {0: 0, 1: 1, 2: 1, 3: 2, 4: 5, 5: 8, 6: 14, 7: 24, 8: 40}

    result = 0
    for i in range(a):
        result += b * dict[i]

    return result

