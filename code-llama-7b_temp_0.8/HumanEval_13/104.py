

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # if a and b are both even, we can cut both in half and find the gcd of half
    # of each number
    while a % 2 == 0 and b % 2 == 0:
        a = a // 2
        b = b // 2
    # otherwise, if both a and b are odd, we can subtract 1 from a and b to get two
    # evens to find the gcd of
    while a % 2 == 1 and b % 2 == 1:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a or b

