
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
    c = []
    a = abs(a)
    b = abs(b)
    while (a > 0):
        c.append(a%10)
        a = a/10
    if b < 10 and c[len(c)-1]*b<0:
        return 0
    else:
        for i in range(len(c)):
            if b < 10:
                c[i] = c[i]*b
            else:
                c[i] = c[i]*b
        return reduce(lambda x,y: x+y, c)
