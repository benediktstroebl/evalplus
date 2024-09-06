

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
    # Use 256 possible bit patterns to test if n is 2^k, then check if n/p is 0
    for bit_pattern in product([0, 1], repeat=256):
        if int(bit_pattern, 2) == n // p:
            return int(bit_pattern, 2) % p
    return 0
