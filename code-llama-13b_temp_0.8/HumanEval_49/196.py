

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
    assert n >= 0
    if n == 0:
        return 1
    n, m = divmod(n, p.bit_length() - 1)
    result = (1 << m) % p
    i = 2
    while n:
        if n & 1:
            result = (result << p.bit_length() - 1) % p
            result = (result + result + pow(2, p.bit_length() - 1, p)) % p
            result = (result + result + pow(2, p.bit_length() - 2, p)) % p
        n >>= 1
        i += 1
    return result

