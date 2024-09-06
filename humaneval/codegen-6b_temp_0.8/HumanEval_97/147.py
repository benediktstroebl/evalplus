
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
    assert isinstance(a, int) or isinstance(a, long)
    assert isinstance(b, int) or isinstance(b, long)
    assert a > 0 and b > 0
    if len(str(abs(a))) == 1:
        return a * b
    elif len(str(abs(a))) > 1:
        return (a % 10) * (b % 10) * result
    a = abs(a)
    b = abs(b)
    if a == 1:
        return b
    elif a == 0:
        return 0
    elif a > 1:
        return (a % 10) * multiply(a / 10, b)
    elif a < 0:
        return -(a % 10) * multiply(a / 10, b)



assert multiply(148, 412) == 16
assert multiply(19, 28) == 72
assert multiply(2020, 1851) == 0
assert multiply(14,-15) == 20



