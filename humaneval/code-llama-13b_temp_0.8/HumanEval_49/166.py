

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
    if not 0 <= n < 31:
        raise ValueError("n should be in range 0 to 30")
    # The usual trick to compute 2^n mod p is to start with 2 and then do a
    # repeated squaring.  If p is prime, then 2^p-1 is a non-zero multiple of p.
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif n%2:
        return (2*modp(n-1, p))%p
    else:
        return modp(n//2, p)**2%p

