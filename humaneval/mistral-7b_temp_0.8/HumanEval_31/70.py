

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    # 用斐波那契数列表示n的因数
    f = 0
    g = 1
    while f <= n:
        if g <= n:
            f = f + g
        else:
            return False
        g = f - g
    return True

