

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a < b:
        a, b = b, a
    div = 2
    while div <= min(a, b):
        if a % div == 0 and b % div == 0:
            return div
        div += 1
    return 1

