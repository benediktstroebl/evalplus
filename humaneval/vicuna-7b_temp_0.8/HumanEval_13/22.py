

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Check if a and b are positive
    if a < 0 or b < 0:
        raise ValueError("One of a and b is negative.")
    # Check if a and b are coprime
    if a == 0 or b == 0 or (a % b != 0):
        raise ValueError("a and b are not coprime.")
    # Find the first common multiple of a and b
    while a % b:
        a //= b
        b //= b
    return b
