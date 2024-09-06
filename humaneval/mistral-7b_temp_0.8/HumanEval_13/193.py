

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a == 0 or b == 0:
        raise ValueError("Greatest common divisor of two integers is not defined for zero")
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    while True:
        if a % b == 0:
            return b
        if b % a == 0:
            return a
        if a > b:
            b, a = a, b

