
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
    n = str(a)
    m = str(b)
    p = ""
    while n or m:
        if n == m:
            a = a * 10
            b = b * 10
            n = n[:-1]
            m = m[:-1]
        elif n % 10 == m % 10:
            p = str(int(n % 10) * int(m % 10) % 10)
            n = n // 10
            m = m // 10
        else:
            p = str(int(n % 10) * int(m % 10) % 10)
            n = n // 10
            m = m // 10
    return p or 0