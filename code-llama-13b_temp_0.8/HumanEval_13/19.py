

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a == 0 or b == 0:
        return max(a, b)

    # get remainder
    if a < b:
        a, b = b, a

    reminder = a % b

    # if reminder is zero then b is GCD of a and b
    if reminder == 0:
        return b

    # else call function again with parameters (b, reminder)
    return greatest_common_divisor(b, reminder)

