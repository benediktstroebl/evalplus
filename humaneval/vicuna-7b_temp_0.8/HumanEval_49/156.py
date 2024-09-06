

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
    # Handle n < 0 and p < 0
    if n < 0:
        n = -n
    if p < 0:
        raise ValueError("Cannot get p < 0")

    # Use the same algorithm as MOD function in C
    # in http://www.nist.gov/dads/HTML/mod.html
    # with some changes to avoid underflow and subnormal
    # results, such as using long arithmetic instead of float

    # Handle p > n
    if p >= n:
        return p - n

    # Calculate q = (p-1) / 2
    q = (p-1) // 2

    # Calculate r = n / q
    r = n // q

    # Calculate t = (n % q) + ((r > 0) - (r < q))
    t = n % q

    # Calculate u = (p-1) % 2
    u = (p-1) % 2

    # Calculate v = (t - u + (p-1) % 2) % 2
    v = (t - u + (p-1) % 2) % 2

    # Calculate the result
    s = (v - t) % p

    return s
