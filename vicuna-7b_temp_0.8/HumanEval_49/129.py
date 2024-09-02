

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
    if n < 0 or p < 0 or n >= 0 or n == 0 or p == 0 or p < 1:
        raise ValueError("Invalid parameters.")
    if n == 0:
        return 1
    if n < p:
        return 0
    if n % p == 0:
        return 0
    return (n // p) + (n % p)
