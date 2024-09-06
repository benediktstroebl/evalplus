def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Iterate through potential factors from 2 to the square root of n
    for potential_factor in range(2, int(n ** 0.5) + 1):
        if n % potential_factor == 0:
            return potential_factor
    # If no factors are found, n must be a prime itself
    return n