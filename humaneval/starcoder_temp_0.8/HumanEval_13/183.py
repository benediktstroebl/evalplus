

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a <= 0 or b <= 0:
        raise ValueError("a and b should be positive integers")
    if b > a:
        a, b = b, a
    while b!= 0:
        remainder = a % b
        a, b = b, remainder
    return a

