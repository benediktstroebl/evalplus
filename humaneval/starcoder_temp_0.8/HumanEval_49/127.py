

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
    assert n >= 0, f"modp(n, p): n = {n} < 0"
    r = 1
    while n:
        if n & 1:
            r = r * p % MOD
        p = p * p % MOD
        n >>= 1
    return r
