
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

    product = 1
    if a == 0 or b == 0:
        return 0
    elif a < 0 and b < 0:
        a = abs(a)
        b = abs(b)
    elif a < 0:
        a = abs(a)
    elif b < 0:
        b = abs(b)
    else:
        pass
    for i in range(1, len(str(a))+1):
        product *= int(str(a)[-i])
    for j in range(1, len(str(b))+1):
        product *= int(str(b)[-j])
    return product
