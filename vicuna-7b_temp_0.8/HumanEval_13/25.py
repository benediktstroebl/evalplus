

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # base case
    if a == 0:
        return b
    elif b == 0:
        return a

    # find the gcd of a and b modulo the other
    while b != 0:
        if a % b == 0:
            return gcd(a, b)
        a, b = b, a % b

    # compute the gcd of a and b
    return gcd(a, b)
