

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
    assert p > 1
    # p = 101
    # n = 3
    base = 1 << n
    result = base % p
    assert result != 0
    while base >>= 1:
        result = (result * 2) % p
    return result
