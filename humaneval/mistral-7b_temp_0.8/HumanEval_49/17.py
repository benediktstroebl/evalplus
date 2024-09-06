

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
    def _pow(x: int, n: int):
        """Return x^n."""
        if n == 0:
            return 1
        if n & 1:
            return _pow(x, n - 1) * x
        else:
            return _pow(x * x, n // 2)

    return _pow(2, n) % p
