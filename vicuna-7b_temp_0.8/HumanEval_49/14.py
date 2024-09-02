

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
    # If n = 0, we have to check that p is not 0.
    if n == 0:
        if p == 0:
            return 1
        # For other values of n, we use the algorithm described above
        return pow(2, n, p)
    else:
        return pow(2, n, p)