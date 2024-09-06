

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # 1. Find the largest prime factor for each of the primes below n
    # 2. Find the greatest of those (f)
    # 3. Find the remainder (r)
    # 4. If r is not 0, then find the largest prime factor of r
    # 5. Repeat until r is 0

    largest_prime = 1
    factor = 2
    while n > 1:
        # Check if n is divisible by the next prime
        if n % factor == 0:
            largest_prime = factor
            n = n // factor
        # Try the next prime
        factor += 1
    return largest_prime

