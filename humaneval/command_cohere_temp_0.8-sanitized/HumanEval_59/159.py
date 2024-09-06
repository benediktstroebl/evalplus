def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest possible factor initially
    divisor = n - 1
    while divisor > 1:
        # Check if the divisor is prime
        if divisor == 2 or divisor & 1:
            return divisor
        divisor //= 2
    return 1