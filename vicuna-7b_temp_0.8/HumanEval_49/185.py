

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
    # Fix for Python 3: Multiplication inside division (or division inside multiplication) can cause problems
    # with negative numbers and integers.
    n = int(n)
    p = int(p)
    if n < 0:
        n *= -1
    if p < 0:
        return 0
    if n % p == 0:
        return 0
    else:
        result = pow(256, n, p)
        if n % 256 == 0:
            result = (result >> 1) % p
        return result % p
