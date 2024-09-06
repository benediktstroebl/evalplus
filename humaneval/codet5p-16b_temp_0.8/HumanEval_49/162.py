

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

    assert n >= 0
    assert p > 2
    ans = 1
    while n:
        if n % 2:
            ans = (ans * 2) % p
        n //= 2
        p = (p * p) % 1000000007
    return ans
