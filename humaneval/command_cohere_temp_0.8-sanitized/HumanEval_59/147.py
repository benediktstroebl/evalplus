def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # The list of primes less than and equal to n.
    primes = [2, 3, 5, 7, 11, 13]
    for prime in primes:
        while n % prime == 0:
            n //= prime
        if n == 1:
            return prime
    return n