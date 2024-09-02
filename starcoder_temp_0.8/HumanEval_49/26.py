

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

    if p <= 0:
        raise ValueError("p should be > 0")

    if n < 0:
        return modp(-n, p)**2 % p

    result = 1
    while n:
        if n & 1:
            result = (result * a) % p
        a = (a * a) % p
        n >>= 1
    return result

