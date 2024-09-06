

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Add your code here
    if a == 0:
        return b
    elif b == 0:
        return a

    if a > b:
        tmp = a
        a = b
        b = tmp

    while b != 0:
        a, b = b, a % b

    return a

