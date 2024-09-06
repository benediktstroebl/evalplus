def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Check for the edge case where n is a power of 2.
    if n >= 2 and ((n & (n - 1)) == 0):
        return 2
    # Script inspired by Python's built-in factorization.
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return i