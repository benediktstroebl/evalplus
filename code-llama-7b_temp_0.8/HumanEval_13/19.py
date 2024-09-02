

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # your task: implement a function greatest_common_divisor(a, b)
    # that returns the greatest common divisor of a and b
    # (the function may use a recursive call)
    # Note that this algorithm finds the greatest common divisor of two integers
    # in a most efficient way
    if a == 0:
        return b
    return greatest_common_divisor(b % a, a)

