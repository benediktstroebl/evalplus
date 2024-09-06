

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
    # Check if n <= 0
    if n < 0:
        raise ValueError("n must be non-negative")
    # Check if p is not zero
    if p == 0:
        raise ValueError("p must be positive")
    # Shift n to the left so that n is non-negative and p is removed from the right
    while n > 0 and p % n == 0:
        n //= p
        p //= p
    # Calculate 2^n modulo p
    return pow(2, n, p)
