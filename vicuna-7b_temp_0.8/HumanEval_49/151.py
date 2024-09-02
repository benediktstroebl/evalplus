

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
    # The division is done in 32 bits, in case p is small.
    x = 0
    for i in range(32):
        x = (x + int(p)) % int(n)
        if x < int(n):
            break
    return x
