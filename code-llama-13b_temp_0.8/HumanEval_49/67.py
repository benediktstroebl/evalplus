

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
    if n == 0:
        return 1
    bit = 1 << (n.bit_length() - 1)  # 2^((n.bit_length() - 1))
    r = 2 if n & bit else 1
    while bit > 1:
        bit >>= 1
        r = (r * r) % p
        if n & bit:
            r = (r * 2) % p
    return r

