

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # Inputs validation
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b should be integers")
    elif a == b:
        return a

    min_num = min(a, b)

    for i in range(1, min_num + 1):
        if a % i == 0 and b % i == 0:
            return i

