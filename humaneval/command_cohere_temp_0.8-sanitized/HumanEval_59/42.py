def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            factor = possible_factor
    # Check for possibility of larger prime factors beyond sqrt(n)
    if n > 10 ** 5 and factor == n // 2:
        factor = 2
    return factor