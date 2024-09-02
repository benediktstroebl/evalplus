

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
    # Get high 1 bits of (p-1)**n (cannot use ** here)
    r, s = divmod(p-1, 2**n-1)
    # r = n or r = 0
    if r == n:
        return 1
    else:
        return 0