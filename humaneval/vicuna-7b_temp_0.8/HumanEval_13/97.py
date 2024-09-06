

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Use the Euclidean algorithm
    # (a,b) = (a0, b0), (a1, b1), ..., (ak-1, bk-1)
    a, b = a0, b0
    if a == 0:
        return 0
    while b != 0:
        q, r = a, b
        a, b = q, (b // r)
        if a == 0:
            return r
    return r
