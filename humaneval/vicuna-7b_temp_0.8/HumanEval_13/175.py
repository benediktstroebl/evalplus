

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # binary GCD
    while a != 0 and b != 0:
        if a % b == 0:
            return a
        elif b % a == 0:
            return b
        a, b = b, a - b % a
    return 1