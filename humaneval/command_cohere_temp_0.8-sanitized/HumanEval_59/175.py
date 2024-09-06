def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Iterate through possible factors from 2 to the square root of n.
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            return possible_factor
            # Exit early if a larger prime factor is found.
    # If no factors found, return n, which must be a prime.
    return n