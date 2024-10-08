

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
    assert 0 <= n < 101
    assert p >= 2
    result = 1
    while n != 0:
        if (n & 1) == 1:
            result = result * result % p
        n >>= 1
        result = result * result % p
    return result

