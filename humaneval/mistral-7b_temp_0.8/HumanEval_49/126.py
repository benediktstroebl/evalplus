

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
    if n < 0:
        n = -n
    assert n < p, f"{n} is larger than {p}."
    n2 = 2 * n
    if n2 > p:
        return 1
    while n2 > 0:
        if n2 > p:
            n2 = n2 - p
        else:
            n2 = n2 // 2
        n = n // 2
    return n
