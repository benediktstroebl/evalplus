def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as the answer
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    # If no even factor found, then n is a prime itself
    return n