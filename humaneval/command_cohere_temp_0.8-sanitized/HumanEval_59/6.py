def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for largest factor first
    largest = n // 2
    for possible_factor in range(3, int(n**0.5) + 1, 2):
        if n % possible_factor == 0:
            largest = possible_factor
    return largest