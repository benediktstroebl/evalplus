

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2 or n % 2 == 0:
        return 1
    # Use the sieve of Eratosthenes to find all prime numbers less than n
    primes = [True]
    for p in range(3, int(n**0.5) + 1):
        if p > n:
            break
        if p % 2 == 0:
            primes[int(p**0.5)::2] = [False]
    # Find the largest prime factor
    largest = 2
    for p in primes:
        if p > largest:
            largest = p
    return largest