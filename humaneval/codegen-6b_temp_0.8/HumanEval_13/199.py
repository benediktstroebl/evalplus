

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if not abs(a) > abs(b):
        return abs(a)
    if not abs(b) > abs(a):
        return abs(b)
    # if a and b are not divisible by each other then return the bigger of the two
    if a % b == 0:
        return b
    # if a is greater than b, then b will be returned
    if a > b:
        return greatest_common_divisor(a - a % b, b)
    else:
        return greatest_common_divisor(a, b - b % a)
