

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # base cases
    if a == 0 or b == 0:
        return 0
    if a % b == 0:
        return a
    # find gcd of b and remainder of a/b
    if b > a:
        return greatest_common_divisor(a, b - a)
    # reverse sub-problem
    return greatest_common_divisor(b, a)
