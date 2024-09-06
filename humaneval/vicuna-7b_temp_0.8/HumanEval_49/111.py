

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
    result = 0
    if n == 0:
        return p
    for i in range(n-1, -1, -1):
        if n % i == 0:
            result += (n // i) // 2
            n = n // i
    return result * (p - 1) % p
