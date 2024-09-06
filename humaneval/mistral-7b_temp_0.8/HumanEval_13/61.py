

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a > b:
        temp = a
        a = b
        b = temp
    for i in range(1, a):
        if a % i == 0 and b % i == 0:
            return i

