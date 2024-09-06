

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Find the largest prime factor of n
    if n <= 1:
        return 1
    # Use a sieve to find the largest prime less than or equal to sqrt(n)
    n_sq = n * n
    sqrt_n = n_sq ** 0.5
    primes = [2]
    for p in range(sqrt_n, n_sq + 1, n_sq):
        primes.append(p)
        if p > 1:
            for i in range(2, p):
                primes.append(i)
    # Return the largest prime factor
    largest_prime = primes[-1]
    for p in primes[:-2]:
        if p > largest_prime:
            largest_prime = p
    return largest_prime
