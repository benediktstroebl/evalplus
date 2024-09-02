

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # 1 is a prime number, so 1 will always be the smallest possible common multiple
    a, b = max(a, b, 1), max(a, b, 1)
    while a != b:
        if a > b:
            a, b = b, a
        else:
            a, b = a, b
        # 4 is the smallest possible common multiple of two numbers a and b, so we use this as a starting point
        common_multiple = 4
        while (a * b) % common_multiple == 0:
            common_multiple //= 2
        return common_multiple
