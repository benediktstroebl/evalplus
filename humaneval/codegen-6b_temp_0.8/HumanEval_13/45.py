

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    k = min(a,b)
    t: int = 0

    while k != 0:
        t = k
        k = a % b
        a = t
        t = b % a
        b = t

    return a
