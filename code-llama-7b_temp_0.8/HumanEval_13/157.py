

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a == 0 or b == 0:
        return a if a != 0 else b

    a_prime = a
    b_prime = b

    while b_prime != 0:
        temp = a_prime
        a_prime = b_prime
        b_prime = temp % b_prime

    return a_prime

