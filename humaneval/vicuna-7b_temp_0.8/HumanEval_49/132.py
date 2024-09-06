

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
    # See also: 
    #   http://graphics.stanford.edu/~seander/bithacks.html#ModPowerTwo
    #   https://en.wikipedia.org/wiki/Modular_arithmetic
    if n < 0:
        return -modp(n, p)
    if p == 0:
        return 1
    elif n < p:
        return 0
    elif n % 2 == 0:
        return p + (n // 2)
    else:
        r = p - (n // 2)
        if n % 4 == 0:
            r += r // 2
        return r
