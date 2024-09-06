

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
    s = 1
    while n > 0:
        if n % 2 == 1:
            s *= s
            if s > p:
                s %= p
        n //= 2
        if s > p:
            s %= p
    return s

