

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # TODO: This is a brute force, try to find a more efficient way
    return 1 if b == 0 else greatest_common_divisor(b, a % b) if a % b == 0 else greatest_common_divisor(b, a)

