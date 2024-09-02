

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
    def bit(n, m):
        return (n >> m) & 1

    def f(n, m):
        if m == 0:
            return 1
        a = f(n, m // 2)
        a = (a * a) % p
        a = (a * (bit(n, m-1) + p)) % p
        return a

    return f(2, n)

