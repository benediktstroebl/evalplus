
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
    res = []
    if a < 10:
        res.append(a * b)
    else:
        res.append(int(a / 10) * int(b / 10))
        if a % 10 - b % 10 == 0:
            res.append(0)
        elif a % 10 > b % 10:
            res.append(10 - (a % 10 - b % 10))
        else:
            res.append(a % 10 - b % 10)
    return int("".join([str(i) for i in res]))

