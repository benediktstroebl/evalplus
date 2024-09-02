

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    min_number = min(a, b)
    greatest_common_divisor = min_number
    while greatest_common_divisor > 1:
        if a % greatest_common_divisor == 0 and b % greatest_common_divisor == 0:
            return greatest_common_divisor
        greatest_common_divisor -= 1
    return greatest_common_divisor

