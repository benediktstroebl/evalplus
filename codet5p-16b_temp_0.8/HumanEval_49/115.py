

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

    print(modp.__doc__)
    assert n >= 0, 'n must be a non-negative integer'
    assert p > 2, 'p must be an odd prime number'
    print(modp.__annotations__)
    return pow(2, n, p)

