

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    i = 1
    while(i <= min(a, b)):
        if (a % i == 0) and (b % i == 0):
            gcd = i
        i = i + 1
    return gcd
