

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
    n_bits = int(log2(n))
    p_bits = int(log2(p))
    if n_bits >= p_bits:
        return (n // p) % p
    return n % p
