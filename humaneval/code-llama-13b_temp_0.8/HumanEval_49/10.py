

def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    # in case the number overflows
    # we have to be smarter here
    # or use the one from the official course:
    # return (1 << n) % p
    # from course
    # return ((1 << n) & ((1 << n) - 1)) % p
    # TODO: is this really working?
    # return ((1 << n) % p) % p
    return ((1 << n) % p)

