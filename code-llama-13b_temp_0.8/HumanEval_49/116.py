

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
    n, p = int(n), int(p)
    if not n:
        return 1
    if n == 1:
        return 2
    bit = 1
    while bit <= n:
        bit <<= 1
    bit >>= 2
    if bit == 1:
        return modp(n, p)
    return ((modp(n - bit, p) << 1) + modp(bit - 1, p)) % p

