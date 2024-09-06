

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
    # see http://stackoverflow.com/questions/530700/python-fastest-way-to-compute-modular-arithmetic-with-large-numbers
    # for implementation details
    remainder = n % p
    while remainder >= p:
        n = n // p
        remainder = n % p
    return remainder
