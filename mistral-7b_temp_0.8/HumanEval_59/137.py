

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # return max(p for p in prime_factors(n) if is_prime(p))
    p = 2
    while n != 1:
        if n % p == 0:
            n /= p
        else:
            p += 1
    return p

