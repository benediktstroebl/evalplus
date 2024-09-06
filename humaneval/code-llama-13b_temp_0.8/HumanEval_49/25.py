

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
    if n >= 1:
        if n < 32:
            return (1 << n) % p
        else:
            res = 1
            while True:
                if n & 1:
                    res = (res * 2) % p
                n >>= 1
                if n == 0:
                    break
                res = (res * res) % p
            return res
    return 1

