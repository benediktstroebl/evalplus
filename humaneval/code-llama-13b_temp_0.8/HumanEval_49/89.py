

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
    bits = []
    while n > 0:
        bits.append(n % 2 == 1)
        n //= 2
    bits = bits[::-1]

    out = 1
    for i in bits:
        out = (out * out) % p
        if i:
            out = (out * 2) % p
    return out

