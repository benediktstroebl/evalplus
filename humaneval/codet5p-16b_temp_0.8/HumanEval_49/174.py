

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

    assert 0 <= n < 2 ** 32, "exponent overflow"
    assert 1 <= p <= 2 ** 32, "modulus overflow"
    return (2 ** n) % p
