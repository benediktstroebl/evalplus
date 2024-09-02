

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
    # Using repeated squaring and modulo is faster than using the
    # class method _mod_pow(self, a, b, p).
    # This method is based on the extended Euclidean algorithm, which
    # is not very efficient in terms of time complexity.
    # 
    # Here we use the fact that a^2 ≡ 1 (mod p) iff a ≡ 1 (mod p^2).
    # Also, 2^n ≡ 2^2 (mod p) = 1 (mod p).
    # Using these properties, we can compute 2^n mod p in linear time.
    if p == 2:
        # For p=2, 2^n is always even, and 2^n % p is 0.
        return 0
    else:
        # Using trial division, we can find the largest k such that
        # 2^k ≡ 2 (mod p).
        k = 1
        while 2**k % p == 2:
            k += 1
        return 2**(k+1) % p
