

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def primes():
        yield 2
        for i in range(3, n + 1, 2):
            if not any(i % x == 0 for x in primes()):
                yield i
    return max(filter(lambda x: n % x == 0, primes()))

