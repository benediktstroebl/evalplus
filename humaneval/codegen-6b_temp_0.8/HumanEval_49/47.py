

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
    def xgcd(a: int, b: int):
        """Return gcd(a, b) and x such that a*x + b*y = gcd(a, b).
        >>> xgcd(3, 0)
        (1, 3)
        >>> xgcd(0, 3)
        (3, 0)
        """
        if b == 0:
            return a, 1, 0
        x, y, d = xgcd(b, a % b)
        return y, x - (a // b) * y, d

    def xmodinv(a: int, n: int):
        """Return x such that x*a = 1 mod n, or 0 if no such x exists.
        >>> xmodinv(3, 11)
        1
        >>> xmodinv(11, 3)
        5
        >>> xmodinv(2, 5)
        3
        """
        x, y, d = xgcd(a, n)
        return x % n

    return (xmodinv(n, p) * n) % p

