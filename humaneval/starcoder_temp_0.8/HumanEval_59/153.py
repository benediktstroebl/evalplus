

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    result = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            result = p
            n = n // p
        else:
            p += 1
    return n
