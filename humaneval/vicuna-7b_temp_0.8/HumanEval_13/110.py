

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # If a is 0, b is even, return b
    if a == 0:
        if b % 2 == 0:
            return b
    # If a is 1, b is odd, return b+1
    else:
        if b % 2 == 0:
            return b + 1
        # If a is not 0 or 1, b is even, return gcd(a,b)
        else:
            return gcd(a,b)
