

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
    lshift = 1
    rshift = 1
    if p > 1:
        lshift = p - 1
    if n % 2:
        rshift = p - 1
    while n > 0:
        n, remainder = divmod(n, p)
        if n == 0:
            break
        n = remainder
        if n % 2 == 0:
            if p == 2:
                result = int(result * lshift + remainder * rshift)
            else:
                result = int(result * lshift + remainder)
        else:
            if p == 2:
                result = int(result * rshift + remainder * lshift)
            else:
                result = int(result * rshift + remainder)
    return result
