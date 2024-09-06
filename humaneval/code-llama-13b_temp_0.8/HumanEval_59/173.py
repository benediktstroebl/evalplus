

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            prime_factors.append(d)
            n = n // d
        d = d + 1
    if n > 1:
        prime_factors.append(n)
    return max(prime_factors)
