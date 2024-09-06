

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    if a == 0 and b == 0:
        raise Exception("It isn't a greatest common divisor for 0 and 0")
    elif a < 0 or b < 0:
        raise Exception("Only positive values are allowed")

    while b != 0:
        a, b = b, a % b
    return a

