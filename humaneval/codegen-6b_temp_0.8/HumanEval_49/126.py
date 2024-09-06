

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
    # b = (n-1) | 1
    # b = n-1 + (n-1) | 1
    # b = n+(n-1) | 1
    # b = n+n+(n-1) | 1
    # b = n+(n+n+n+n+n-1) | 1
    # https://en.wikipedia.org/wiki/Digital_root
    # c = 0
    # while n:
    #     c = c+1
    #     n = (n-1) & n
    # b = c
    # if b % 2:
    #     b += 1
    # return b
    if n == 0:
        return 1
    else:
        return (n & (n - 1)) + modp(n - (n & (n - 1)), p)
