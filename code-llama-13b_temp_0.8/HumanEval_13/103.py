

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    assert isinstance(a, int) and isinstance(b, int), 'expected int'
    assert a >= 0 and b >= 0, 'expected non-negative int'
    if a == 0 and b == 0:
        return 0
    if a == 0 or b == 0:
        return max(a, b)
    return greatest_common_divisor(b, a % b)

