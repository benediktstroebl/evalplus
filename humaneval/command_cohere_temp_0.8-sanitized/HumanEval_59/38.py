def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Precompute prime numbers using Sieve of Eratosthenes
    # Limit is the largest number that is qualify as a prime factor for n.
    LIMIT = int(n ** 0.5) + 1
    primes = {}
    for i in range(2, LIMIT + 1):
        if primes:
            for j in primes:
                if i * j <= LIMIT:
                    primes[j] = i * j
        else:
            primes[i] = i
    # Now, we directly extract the largest prime factor
    # by dividing n by all prime factors up to the limit
    largest_prime = n
    for i in primes:
        if n % i == 0:
            largest_prime //= i
    if largest_prime > 1:
        largest_prime *= primes[largest_prime]
    return largest_prime