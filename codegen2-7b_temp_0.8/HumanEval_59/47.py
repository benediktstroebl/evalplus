

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for prime in primes:
        if n % prime == 0:
            return prime
    else:
        return n

