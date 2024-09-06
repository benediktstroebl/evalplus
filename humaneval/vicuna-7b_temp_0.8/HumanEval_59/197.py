

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # We use the Sieve of Eratosthenes to find all prime numbers less than sqrt(n).
    # Then we check each of these numbers to see if they are factors of n.
    sqrt_n = int(np.sqrt(n))
    primes = [x for x in range(2, sqrt_n + 1) if x % 2 == 1]
    for p in primes:
        if n % p == 0:
            return max(p, 2)
    return 2
