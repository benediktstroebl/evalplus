

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # return a greatest common divisor of two integers a and b

    if a < 0 or b < 0:
        raise ValueError('Некорректные данные')
    if a == 0 or b == 0:
        return 0
    if a == b:
        return a
    while a != b:
        if a > b:
            a -= b
        elif a < b:
            b -= a
    return a

