

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def prime_factors(n):
        for i in range(2,n):
            while n%i == 0:
                yield i
                n = n/i
        if n > 2:
            yield n
    return max(prime_factors(n))

