def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Handle the case where n is a power of 2.
    if n >= 2 and ((n & (n - 1)) == 0):
        return 2
    # Handle other potential edges
    for potential_factor in [3, 5, 7, 13, 19, 23, 29, 31, 37]:
        if n % potential_factor == 0:
            return potential_factor
    # Check from the square root of n
    for potential_factor in range(int(n**0.5) + 1, 0, -1):
        if n % potential_factor == 0:
            return potential_factor
    # If none of the above, n must be a prime
    return n