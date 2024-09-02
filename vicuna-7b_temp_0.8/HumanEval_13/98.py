

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # This is a simple Euclidean algorithm implementation
    # We use the gcd of two numbers as a factor for the gcd of the sum
    # of two numbers a and b
    return gcd(b, a - b)
