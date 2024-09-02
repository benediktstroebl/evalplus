

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
    # If n is 0 or p is 0, return 1
    if n == 0 or p == 0:
        return 1
    else:
        # If p is odd, we can use the formula x = x^(p-1) + ... + x^2 + x + 1
        if p&1:
            return pow(n,p-1,p) + pow(n,p-2,p) + ... + pow(n,p-1,p)
        else:
            return pow(n,p-1,p)
