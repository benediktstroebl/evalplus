
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
    a = str(a)
    b = str(b)
    res = [int(x) * int(y) for x,y in zip(a,b)]
    unit = [int(x) for x in str(sum(res))]
    return reduce(lambda x,y: x*10+y, unit)
    # return reduce(lambda x,y: x*10+y, map(int, str(sum(res))))
