

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    min_num = min(a, b)
    max_num = max(a, b)
    for i in range(1, min_num + 1):
        if max_num % i == 0 and min_num % i == 0:
            gcd = i
    return gcd
