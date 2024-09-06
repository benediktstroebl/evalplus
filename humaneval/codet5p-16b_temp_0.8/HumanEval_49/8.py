

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

    bin_n = bin(n)
    bin_p = bin(p)
    mod_n = bin_n[2:len(bin_n)]
    mod_p = bin_p[2:len(bin_p)]
    if mod_n[0] == '0':
        mod_n = '1' + mod_n
    if mod_p[0] == '0':
        mod_p = '1' + mod_p
    pow = 1
    for i in range(1, len(mod_p)):
        pow *= 2
        if mod_p[i] == '1':
            pow = (pow*2) % p
    return pow % p
