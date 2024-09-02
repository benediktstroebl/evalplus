

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
    assert 1 <= p <= 100, 'p must be between 1 and 100.'
    assert 0 <= n < 100, 'n must be less than 100.'
    if n < 1:
        return 1
    else:
        if n % 2 == 0:
            return (modp(n // 2, p) ** 2) % p
        else:
            return ((modp(n // 2, p) ** 2) % p) * (n % 2) % p

