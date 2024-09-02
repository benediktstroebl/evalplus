

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # your task: implement this function
    # the function should be implemented in O(log(max(a, b)))
    # see, that we are using max built-in function to get the greater number among a and b
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return greatest_common_divisor(b, a % b)

