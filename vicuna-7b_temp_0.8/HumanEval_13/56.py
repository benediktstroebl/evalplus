

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # use Euclidean algorithm to find the GCD of a and b
    # here we assume that the two integers are relatively prime
    # to avoid potential issues with the algorithm
    if a == 0:
        return b
    if b == 0:
        return a
    gcd = a
    x = b
    while x != 0:
        gcd, x = x, gcd % x
    return gcd
