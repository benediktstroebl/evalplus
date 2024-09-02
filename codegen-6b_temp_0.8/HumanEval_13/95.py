

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if not (a and b):
        return 0
    if a == b:
        return a
    greatest_divisor = 1
    for i in range(min(a, b), 0, -1):
        if a % i == b % i == 0:
            greatest_divisor = i
            break
    return greatest_divisor
