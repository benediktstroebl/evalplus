
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
    #Handle the special case of 0 and -1
    if b == 0 or b == -1:
        return 0
    elif a % 10 == 0 and b % 10 == 0:
        return (int(a) / 10) * (int(b) / 10)
    else:
        return (int(a) * (10 - int(b))) // 10