

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
    assert 0 <= n < p, f"n ({n}) must be between 0 and {p - 1} (inclusive)"
    s = []
    s.append(1)
    s.append(n)
    while True:
        s.append((s[0] + s[1]) % p)
        s.append((s[0] * s[1]) % p)
        if s[1] == 0:
            return s[0]
        s[0], s[1] = s[1], s[0]

