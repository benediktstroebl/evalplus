

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
    n = n % ((p * 7) // 4)
    if n <= 0:
        return 1
    a = 2
    b = 4
    while True:
        if n & 1:
            b = b * a % p
        n = n >> 1
        if n == 0:
            break
        a = a * a % p
    return b

