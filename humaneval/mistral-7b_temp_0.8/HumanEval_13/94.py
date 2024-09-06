

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    if a < 0 or b < 0:
        raise ValueError("a and b should be non-negative")
    if a == 0 or b == 0:
        raise ValueError("a and b should not be 0")

    if a == b:
        return a

    if a > b:
        return greatest_common_divisor(b, a)

    if a % b == 0:
        return b

    return greatest_common_divisor(b, a % b)

