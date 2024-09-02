

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
    # Hint: use binary arithmetic.
    # If you do binary arithmetic, then 2^n mod p is easily calculated by multiplying
    # 2 to itself n times and then taking the result modulo p.
    n_bits = n.bit_length()
    res = 1
    for _ in range(n_bits):
        res = res * 2
        res = res % p
    return res

