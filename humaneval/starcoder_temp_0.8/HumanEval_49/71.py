

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

    bin_n = format(n, 'b')
    bin_n = '0' * (len(bin_n) - len(bin_n.rstrip('0'))) + bin_n.rstrip('0')

    res = 0

    for i, digit in enumerate(bin_n):
        if digit == '1':
            res += pow(2, i)

    return res % p
