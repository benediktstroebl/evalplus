def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Make a list of the prime factors of n: excludes 1, divides n exactly
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
    # Return the largest factor which is also the largest prime factor
    return max(factors)