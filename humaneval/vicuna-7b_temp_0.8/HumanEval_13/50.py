

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # binary GCD algorithm
    if a < b:
        a, b = b, a
    while a != 0 and b != 0:
        if a % b == 0:
            a //= b
            b //= b
        else:
            b, a = a, b
    return a
