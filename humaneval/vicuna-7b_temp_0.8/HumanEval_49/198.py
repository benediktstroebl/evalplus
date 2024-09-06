

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
    # compute GCD(2^n, p) and store in q
    q, r = ec_point_mul(curve, p, n)
    if r == 0:
        # compute 2^n modulo the GCD(2^n, p)
        return pow(2, n, q, modulo=p)
    else:
        # 2^n is congruent to r modulo p
        return pow(2, n, q) % p
