

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a < 0 or b < 0:
        return 0

    # if a and b are both positive, check if they are equal
    if a == b:
        return a

    # if a and b are both non-zero, check if their absolute values are equal
    abs_a = abs(a)
    abs_b = abs(b)
    if abs_a == abs_b:
        return abs_a

    # if a and b are not equal and their absolute values are not equal,
    # then they are not relatively prime
    return 0