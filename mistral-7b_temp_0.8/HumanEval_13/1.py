

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # gcd of 0 and 0 is 0
    if a == 0 and b == 0:
        return 0

    # gcd of a and b is a if b is 0
    if b == 0:
        return a

    # gcd of a and b is b if a is 0
    if a == 0:
        return b

    # Check if a and b have the same sign
    a_sign = a > 0
    b_sign = b > 0

    # Compute the gcd of abs(a) and abs(b)
    gcd = greatest_common_divisor(abs(a), abs(b))

    # Return the sign of a if it is positive or the sign of b if it is negative
    return gcd if a_sign else -gcd

