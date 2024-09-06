

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

    n_bin = bin(n)[2:]
    n_bin = n_bin[::-1]
    n_bin = n_bin[:len(n_bin)-1]
    n_mod = 0
    for i in range(len(n_bin)):
        n_mod = n_mod + int(n_bin[i])*2**i

    return n_mod % p
