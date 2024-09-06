def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for largest factor first which is not a prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i