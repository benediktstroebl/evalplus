
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
    m = [int(i) for i in str(a)]
    n = [int(i) for i in str(b)]

    if len(m) > len(n):
        n = ['0' for i in range(0, len(m) - len(n))] + n

    elif len(n) > len(m):
        m = ['0' for i in range(0, len(n) - len(m))] + m

    l = [int(i) * int(j) for i, j in zip(m, n)]
    return sum(l)

