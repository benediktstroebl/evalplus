

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    primes = {}
    for x in range(2, n):
        if n % x == 0 and (x in primes or x==2):
            primes[x] = True
            if x > n // x:
                return n // x
    return 1 if n > 1 else n

