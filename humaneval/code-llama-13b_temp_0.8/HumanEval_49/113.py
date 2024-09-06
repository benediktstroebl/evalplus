

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
    assert p > 1, f"invalid p={p}"
    assert 0 <= n < p, f"invalid n={n} for p={p}"
    if n == 0:
        return 1
    res = 2
    for _ in range(1, n):
        res = (res * res) % p
    return res

