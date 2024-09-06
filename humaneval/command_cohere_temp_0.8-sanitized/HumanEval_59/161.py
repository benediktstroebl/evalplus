def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest possible factor first. This avoids wasting efforts on multiples.
    max_divisor = n // 2
    for divisor in range(3, int(n**0.5) + 1, 2):
        while n % divisor == 0:
            n //= divisor
        if n == 1:
            return divisor
    if n > 1:
        return n