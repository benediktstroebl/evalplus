

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
    # Checks
    if n < 0 or p < 2:
        return None

    n, p = int(n), int(p)
    m, acc = 1, 1

    # First bit
    while n:
        n, last = divmod(n, 2)
        if last:
            acc = (acc * m) % p
        m = (m * m) % p

    return acc
