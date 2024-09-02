

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # divide by 2 repeatedly until one of the values is zero
    while a or b:
        if a > b:
            a //= 2
            b //= 2
        elif b > a:
            b //= 2
            a //= 2
        else:
            break
    return a if b % a == 0 else b
