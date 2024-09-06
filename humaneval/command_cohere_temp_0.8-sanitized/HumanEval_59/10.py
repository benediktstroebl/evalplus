def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Check for the edge case where n is a power of 2.
    if n >= 2 and ((n & (n - 1)) == 0):
        return 2
    # Iterate through 2, 3, 5, 7, ..., sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            n //= i
    # If n > 2 and n is a prime, return n
    if n > 2 and n == 3:
        return 3
    # At this point, n must be a prime greater than 2
    return n