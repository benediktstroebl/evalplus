def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Handle the case where n is a power of 2.
    if n > 2 and ((n & (n - 1)) == 0):
        return 2
    # Traverse through divisors up to the square root of n.
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i