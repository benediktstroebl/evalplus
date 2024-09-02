

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
    # Ensure p is positive
    if p < 0:
        raise ValueError("p should be positive")

    # Ensure n is non-negative
    if n < 0:
        raise ValueError("n should be non-negative")

    # Ensure n is less than p
    if n > p:
        raise ValueError("n should be less than p")

    # Calculate 2^n
    two_n = 2 ** n

    # Calculate 2^n modulo p
    result = two_n % p

    return result
