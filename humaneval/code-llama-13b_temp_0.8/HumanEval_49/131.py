

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
    n = int(n)
    p = int(p)
    if n < 0:
        raise ValueError(f"negative n: {n}")
    if p <= 0:
        raise ValueError(f"non-positive p: {p}")
    x = 1
    while n != 0:
        if n % 2 == 1:
            x = (x * x) % p
        n //= 2
        x = (x * x) % p
    return x

