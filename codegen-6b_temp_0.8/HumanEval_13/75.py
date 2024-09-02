

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # greatest common divisor of two integers a and b is the largest integer that divides
    # both integers
    if a == 0 and b == 0:
        return 0
    if a == 0:
        return b
    if b == 0:
        return a
    elif a > b:
        return greatest_common_divisor(a - b, b)
    else:
        return greatest_common_divisor(a, b - a)

