

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
    # if p is a prime:
    #  1, p - 1
    if p == 2:
        return 1
    if p % 2 == 0:
        return 1
    m = p - 1
    while m % 2 == 0:
        m = m // 2
    assert m % 2 == 1
    t = 1
    for i in range(n + 1):
        t = (t * t) % p
        if m % 2 == 1:
            t = (t * 2) % p
        m = m // 2
    return t

