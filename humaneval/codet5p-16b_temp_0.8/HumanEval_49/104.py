

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
        raise ValueError("n must be a non-negative integer.")
    if p <= 1:
        raise ValueError("p must be an integer that is greater than 1.")
    if not n & (n - 1):  # if n is a power of 2
        return n % p
    elif p == 2:  # if p is 2
        return n  # since n % p == 0
    else:  # if p is neither
        return (modp(n, p - 1) * modp(n, p)) % p

