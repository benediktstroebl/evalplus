def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Checkout the first element in the factor list. This is the largest factor
    for potential_factor in range(2, int(n ** 0.5) + 1):
        if n % potential_factor == 0:
            n //= potential_factor
        else:
            return potential_factor
    # If we reach here, the largest factor is n itself
    return n