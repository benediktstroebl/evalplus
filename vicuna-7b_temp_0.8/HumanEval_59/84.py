

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Try to find a prime using trial division
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    # If not found, use the Sieve of Eratosthenes to find the largest prime factor
    sieve = [True for i in range(int(n ** 0.5) + 1)]
    for p in range(3, int(n ** 0.5) + 1):
        if sieve[p]:
            for q in range(p, int(n ** 0.5) + 1, p):
                sieve[q] = False
    return sieve[int(n ** 0.5)]