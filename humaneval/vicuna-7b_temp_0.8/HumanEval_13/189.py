

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Check if a and b are positive
    if a < 0 or b < 0:
        raise ValueError("a and b must be non-negative integers")

    # Compare a and b repeatedly until we find a non-negative integer x such that a % x == 0 and b % x == 0
    while True:
        if a % b == 0:
            return b
        if a % a == 0:
            return a
        a, b = b, a // b
