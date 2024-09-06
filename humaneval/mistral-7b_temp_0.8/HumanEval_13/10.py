

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    def gcd_iter(a: int, b: int) -> int:
        """Return a greatest common divisor of two integers a and b
        >>> gcd_iter(3, 5)
        1
        >>> gcd_iter(25, 15)
        5
        """
        if a % b == 0:
            return b
        return gcd_iter(b, a % b)

    return gcd_iter(a, b)
