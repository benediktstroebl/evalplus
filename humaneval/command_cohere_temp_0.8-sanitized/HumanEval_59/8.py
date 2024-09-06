def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Check for largest factor first which is not a prime number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    # If no factors are found, return n which is the largest factor
    return n