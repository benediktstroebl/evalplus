

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n == 1:
        return n
    prime_factors = []
    for p in range(2, n):
        if n % p == 0:
            prime_factors.append(p)
    return prime_factors[-1]
