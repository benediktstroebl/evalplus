

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
    # optimization for small n and p
    if n < 0 or n > 31 or p < 2 or p > 1000000:
        return pow(2, n, p) % p

    # for larger values we use iterative approach
    i = 0
    while p >= 2:
        if p % 2 == 0:
            result = pow(2, n, p) % p
            if result == 0:
                return pow(2, n, p - 2) % p
            i += 1
        p /= 2
    result = pow(2, n, p) % p
    if i > 0:
        result = (result >> i) % p
    return result