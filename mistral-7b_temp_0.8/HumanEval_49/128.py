

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
    def fast_pow(b, e, p):
        res = 1
        while e:
            if e % 2:
                res = (res * b) % p
            b = (b * b) % p
            e //= 2
        return res

    return fast_pow(2, n, p)
