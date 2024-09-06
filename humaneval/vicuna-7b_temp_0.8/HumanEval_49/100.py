

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
    # You can use sieve.is_prime(p) to check if p is prime
    # But you can't use p.is_prime() because it's a method on Integer
    # So, you can use is_prime(p, as_int=True) and pass 1 as the second argument
    if not is_prime(p, as_int=True):
        return 0
    else:
        if n > 0:
            return pow(2, n, p)
        else:
            return pow(2, -n, p)
