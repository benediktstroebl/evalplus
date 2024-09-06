

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
    if n < 0 or p < 0:
        raise ValueError("n and p must be positive")
    if n == 0:
        return 1
    if p == 2:
        return 0
    return 2 ** n % p

