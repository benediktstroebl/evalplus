

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # check if a,b are positive integers
    if a < 0 or b < 0:
        raise ValueError("a and b must be non-negative integers")
    # check if a,b are not equal
    if a == b:
        raise ValueError("a and b must be different integers")
    # check if b is a factor of a
    if a % b == 0:
        raise ValueError("a and b must have no common factors")
    # try to find the greatest common divisor using Euclid's algorithm
    while b > 0:
        if b % a == 0:
            gcd = b
            a = b
        else:
            a = a - b
    return gcd
