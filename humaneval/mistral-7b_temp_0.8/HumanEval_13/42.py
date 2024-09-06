

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    assert 0 <= a and 0 <= b
    if a < 0 or b < 0:
        return None
    if a == b:
        return a
    if a > b:
        return greatest_common_divisor(a - b, b)
    return greatest_common_divisor(a, b - a)
