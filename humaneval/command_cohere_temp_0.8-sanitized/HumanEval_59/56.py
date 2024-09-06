def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as the last digit
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    # If no even factors, then n is a prime itself
    return n