

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # STEP 1: Remove one of the numbers to make it odd
    while not (a % 2 and b % 2):
        a, b = a//2, b//2
    # STEP 2: Divide one by the other until one is zero
    while b:
        a, b = b, a % b
    return a

