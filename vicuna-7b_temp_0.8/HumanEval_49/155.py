

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
    # Fast case for small p
    if p < 10000:
        # Efficient modular exponentiation algorithm for p < 10000
        x = 1
        y = n
        while y > 0:
            x = (x * x) % p
            y //= 2
        return x
    # Average case for larger p
    else:
        # Avoid costly modular division with large p
        r = n
        m = 1
        for i in range(10000, len(str(p)) + 1):
            m *= p
            r %= m
        return r
