

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    for prime in primes():
        if n % prime == 0:
            n /= prime
            while n % prime == 0:
                n /= prime
            return prime
    return n

