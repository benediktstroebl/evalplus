

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
    if n < p:
        return n
    if n == p:
        return 1

    # 2**n % p
    n_mod_p = 1
    # 2**n
    n_two = 2
    # 2**(n/2)
    n_two_half = 2**(n//2)

    # Padic representation of 2**n
    n_pow_p = 1
    # 2**(n-1) % p
    n_one_mod_p = n_mod_p

    # 2**(n-1)
    n_one = n_two
    # 2**(n-2)
    n_two_minus_one = n_one // n_two
    # 2**(n-2) % p
    n_one_minus_one_mod_p = n_one_mod_p // n_two

    # 2**(n-4)
    n_two_minus_two = n_two_minus_one // n_two
    # 2**(n-4) % p
    n_one_minus_one_minus_one_mod_p = n_one_minus_one_mod_p // n_two

    while n_two_half > 1:
        # n_pow_p = (n_pow_p*n_pow_p) % p
        n_pow_p = n_pow_p * n_pow_p
        # n_two_half = n_two_half // n_two
        n_two_half = n_two_half // n_two
        # n_mod_p = (n_mod_p*n_two_minus_one) % p
        n_mod_p = n_mod_p * n_two_minus_one
        n_mod_p = n_mod_p % p
        # n_one_mod_p = (n_one_mod_p*n_two_minus_two) % p
        n_one_mod_p = n_one_mod_p * n_two_minus_two
        n_
