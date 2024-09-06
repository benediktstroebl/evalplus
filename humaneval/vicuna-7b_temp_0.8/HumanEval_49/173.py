

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
    # Handle 0
    if n == 0:
        return 0
    # Handle 1
    if n == 1:
        return p
    # Handle 2^n
    x = 0
    while (n >> i) >= 0:
        x = (x * p) % p
        i += 1
    return x
