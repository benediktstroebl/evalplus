
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
    if a > 0:
        a = str(a)
    if b > 0:
        b = str(b)
    if len(a) > 1 and len(b) > 1:
        return (int(a[0])*int(b[0])) + multiply(int(a[1:]), int(b[1:]))
    elif len(a) > 1:
        return int(a[0])*int(b) + multiply(int(a[1:]), b)
    elif len(b) > 1:
        return int(a)*int(b[0]) + multiply(a, int(b[1:]))
    else:
        return int(a)*int(b)

