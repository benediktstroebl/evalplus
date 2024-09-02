

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # find largest prime factor of n.
    def prime_factors(n):
        for i in range(2, n+1):
            while n % i == 0:
                yield i
                n /= i
    prime_factors = prime_factors(n)
    largest_prime = next(prime_factors)
    return largest_prime

