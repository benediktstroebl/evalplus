def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as the largest prime factor
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i