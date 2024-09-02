

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def sieve(n):
        """Generate a list of primes smaller than n.
        >>> sieve(100)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        """
        # primes is a list of primes smaller than n.
        primes = [2]
        while primes[-1] * primes[-1] <= n:
            for i in range(primes[-1], n+1, primes[-1]):
                primes.append(i)
        return primes
    primes = sieve(n)
    for p in primes:
        while n % p == 0:
            n //= p
    return n

