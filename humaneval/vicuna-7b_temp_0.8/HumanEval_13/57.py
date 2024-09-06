

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # if a and b are even then they have a greatest common divisor of 1
    if a % 2 == 0 and b % 2 == 0:
        return 1
    # if a and b are odd then we can use the Euclidean algorithm
    # to find their greatest common divisor
    while b > 0:
        a, b = b, a % b
    return a