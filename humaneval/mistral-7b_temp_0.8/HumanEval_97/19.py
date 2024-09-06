
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
    # your code here
    a = str(a)
    b = str(b)
    c = [int(i) for i in a]
    d = [int(i) for i in b]
    # c = []
    # d = []
    # for i in a:
    #     c.append(int(i))
    # for i in b:
    #     d.append(int(i))
    #
    return int(str(c[0]) + str(d[0]))
