

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
    # The sequence is 2, 3, 2, 8, 3, 2, 8, 3, 2, 8, 3, 2, 8, 3, 2, 8, ...
    # It's not clear at first sight that this is periodic with period 15.
    # It's not even obvious that all terms are distinct.
    # (The last term is 2, so the period is a multiple of 8.)
    assert p > 1
    assert n >= 0
    assert (n < p) or (n % p == 0)
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n % 2 == 0:
        return modp(n // 2, p) ** 2
    else:
        return modp(n - 1, p) * modp(n // 2, p) ** 2

