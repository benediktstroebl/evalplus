

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    assert isinstance(a, int) and isinstance(b, int)
    assert a >= 0 and b >= 0
    assert a % 2 == 1 or b % 2 == 1
    if a % 2 == 0:
        a = a // 2
    if b % 2 == 0:
        b = b // 2
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a + b

