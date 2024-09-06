

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
    if n >= 100:
        raise ValueError("n must be < 100.")
    # get residue of n
    n = n % 100
    # get 2^n (binary representation)
    n_bits = bin(n)[2:]
    # compute 2^n mod p
    res = 1
    for bit in n_bits:
        res = res * res % p
        if bit == '1':
            res = res * p % p
    return res

