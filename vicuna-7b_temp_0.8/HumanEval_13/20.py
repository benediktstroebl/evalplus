

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
    # use Euclid's algorithm to find the gcd
    else:
        return greatest_common_divisor(a, b % a)