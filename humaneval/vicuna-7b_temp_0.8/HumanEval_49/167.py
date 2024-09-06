

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
    # Fast case: m < p
    if n < p:
        return n % p
    # Iterative case: m >= p
    if n >= p:
        p -= 1
        while p < n:
            p = modp(n - p, p)
        return p
    # Invert modular exponentiation
    n_bits = len(str(n))
    r, d = 0, n
    while d < n:
        d, r = modp(d, d * d % n), r * d % n
    return r
