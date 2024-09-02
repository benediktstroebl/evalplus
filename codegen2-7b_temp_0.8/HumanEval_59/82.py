

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while True:
        for candidate in primes:
            if n % candidate == 0:
                n /= candidate
                break
        else:
            return n

