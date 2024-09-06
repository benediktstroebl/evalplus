

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
    # ensure non-negative n
    if n < 0:
        return modp(-n, p)
    # set initial value
    result = 1
    # perform exponentiation
    while n:
        if n % 2:
            result = result * p
        p = p * p
        n = n // 2
    return result

