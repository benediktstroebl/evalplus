

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
    # https://en.wikipedia.org/wiki/Modulo_operation#Right_inverse_for_powers_of_2
    n = n % p  # to ensure n is positive
    # get power of 2 that is less than p
    p_power = 1
    while p_power < p:
        p_power <<= 1
    n_power = n
    # n_power = n * 2^(p-1) = 2^(p-1) * n mod(p)
    n_power = n_power * (1 << (p - 1))
    # n_power = 2^(2*p-2) * n mod(p)
    n_power = n_power * (1 << (p - 2))
    # n_power = 2^(3*p-4) * n mod(p)
    # etc.
    # n_power = (2^(p-1) * n) mod(p)
    while p_power > 1:
        p_power >>= 1
        n_power = n_power * 2 % p
    # n_power = n * 2^0 = n mod(p)
    return n_power

