

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
    # Avoid the overhead of computing n % p
    if n < p:
        return 0
    result = (n % p) // 2**(p-1) + 1
    if n < p:
        result = (result * 2**(p-1)) % p
    return result