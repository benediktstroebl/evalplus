

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
    # If n is zero, the result is 1
    if n == 0:
        return 1

    # If n is even, the result is 1
    if n & 1 == 0:
        return 1

    # If n is odd and p is 1, the result is 1
    if p == 1:
        return 1

    # If n is odd and p is 2, the result is 1
    if n & 1 == 1 and p == 2:
        return 1

    # If p is odd, the result is 2
    if p & 1 == 1:
        return 2

    # If p is even, the result is -2
    if p & 1 == 0:
        return -2

    # Recurse
    return 2 * modp(n // 2, p) * modp(n // 2, p)

