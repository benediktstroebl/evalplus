def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Countdown from max int to n in steps of 2
    for i in range(n, 0, -2):
        if n % i == 0:
            n //= i
    # Returns n if n is a prime
    return n