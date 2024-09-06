

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

    k, result = n, 1
    while k > 0:
        if k % 2 == 0:
            result = (result * 2) % p
        else:
            result = (result * n) % p
        k = k // 2
    return result
    
    
