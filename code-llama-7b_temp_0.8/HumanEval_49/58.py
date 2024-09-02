

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
    # if p == 2:
    #     return 1 if n & 1 else 0
    # return pow(2, n, p)
    x = 1
    for _ in range(n):
        x = (x * 2) % p
    return x


