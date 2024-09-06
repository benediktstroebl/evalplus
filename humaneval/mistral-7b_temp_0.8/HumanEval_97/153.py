
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

    x = str(a)
    y = str(b)
    res = 0

    if int(x[-1]) == 0 or int(y[-1]) == 0:
        return res

    for i in x[-1:]:
        for j in y[-1:]:
            res += int(i) * int(j)

    return res
