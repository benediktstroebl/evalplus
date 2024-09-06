

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Use Euclidean algorithm until the gcd is found
    if a < b:
        a, b = b, a
    while b != 0:
        q, r = b, a % b
        a, b = b, r
    return q