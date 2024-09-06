def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest possible factor before descending down
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    elif n % 5 == 0:
        return 5

    # Checking through all prime numbers that are less than n's square root
    for potential_factor in range(7, int(n ** 0.5) + 1, 2):
        if n % potential_factor == 0:
            return potential_factor

    # If no factors are found, n must be a prime itself
    return n