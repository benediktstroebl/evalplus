

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

    assert 0 <= n and p > 2
    k = 1
    while n > 0:
        if n % 2 == 1:
            k = k * 2 % p
        n //= 2
    return k
