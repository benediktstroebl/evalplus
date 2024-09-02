

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
    from itertools import count
    from math import log
    from sys import maxsize
    i = 1
    while True:
        x = (i*i) % p
        if x == 1:
            break
        i += 1
    if x == 0:
        return 0
    n = n % i
    if n < 0:
        n += i
    if n == 0:
        return 1
    n = 1 << n
    if p < n:
        n = 1 << (n - p)
    if p < 0:
        return -1
    ret = 1
    if n == 1:
        return 0
    i = 0
    while True:
        if ret & 1:
            ret = (ret * x) % p
        x = (x * x) % p
        i += 1
        if n < maxsize:
            n >>= 1
        else:
            n = 1 << (n - p)
        if n == 0:
            return ret


