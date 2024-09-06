def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Coprime decomposition:
    # Iterate through possible factors from 2 to n-1.
    # For each potential factor, if it is coprime with the remainder of n after division by it, then it is the answer.
    for potential_factor in range(2, n):
        if gcd(potential_factor, n % potential_factor) == 1:
            return potential_factor
    # If no factor is found, n is a prime.
    return n