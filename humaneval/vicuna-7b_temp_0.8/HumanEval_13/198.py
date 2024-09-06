

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while True:
        gcd = a
        x = b
        for i in range(1, min(len(a), len(x))):
            if a % x == 0 and x % i != 0:
                gcd = x
                x = i
        if gcd > b:
            return gcd
        b, a = a, b % a
