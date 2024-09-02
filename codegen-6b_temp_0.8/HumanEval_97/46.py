
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
    m = abs(a)*abs(b)
    a = abs(a)
    b = abs(b)
    if a>b:
        div = a
    else:
        div = b
    # print a,b,div
    L = [int(i%div) for i in range(m)]
    # print L
    prod = 1
    for i in L:
        prod *= i
    return prod
