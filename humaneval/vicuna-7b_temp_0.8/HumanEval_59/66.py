

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n <= 1:
        return 1

    n = abs(n)
    factors = factors(n)

    # find the largest prime factor
    p = max(factors, key=lambda x: x.p != 2 and (x.p - 1) % x.q)

    return p
