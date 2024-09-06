def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Look for divisors from largest to smallest until finding a prime divisor
    for potential_divisor in range(1, int(n ** 0.5) + 1):
        if n % potential_divisor == 0:
            n //= potential_divisor
            if potential_divisor > 1 and potential_divisor % 1 == 0:
                return potential_divisor
    if n > 1 and n % 1 == 0:
        return n