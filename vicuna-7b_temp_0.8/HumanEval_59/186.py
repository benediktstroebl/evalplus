

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Check that n is not a prime and greater than 1
    if n > 1 and n % 2 == 0:
        return 2
    # Find the largest prime factor of n by recursively dividing n by its prime factors
    # until we find one that is greater than n / 2
    while True:
        # Divide n by its prime factors in order of increasing size
        for i, p in enumerate(primes_within(n // i + 1)):
            if n % p == 0:
                return p
        # If we reach the end of the loop without finding a prime factor greater than n / 2,
        # then there is no largest prime factor and return 2
        if n != 1:
            return 2
