

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Use Euclid's algorithm to find the GCD of a and b
    # We keep track of a and b, as well as the current GCD and the next GCD
    a_next, b_next, gcd = a, b, 1
    while b_next % a_next != 0:
        gcd, a_next, b_next = b_next, a_next, gcd + b_next // a_next
    return gcd
