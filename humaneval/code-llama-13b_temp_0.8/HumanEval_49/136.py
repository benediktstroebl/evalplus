

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
        raise ValueError("n must be non-negative")
    if p < 2:
        raise ValueError("p must be greater than 1")
    ans = 1
    while n > 0:
        if n & 1:
            ans = (ans * 2) % p
        n = n >> 1
        ans = (ans * ans) % p
    return ans

