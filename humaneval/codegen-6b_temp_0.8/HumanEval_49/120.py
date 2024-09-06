

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
    def _modp(b):
        if b == 0:
            return 1
        if b % 2 == 0:
            # exponent in 2 is even
            return (2 * _modp(b / 2)) % p
        else:
            return (3 * _modp((b - 1) / 2)) % p

    return _modp(n)

