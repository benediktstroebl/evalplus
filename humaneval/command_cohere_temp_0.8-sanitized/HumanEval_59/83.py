def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            factor = possible_factor
    # Check for an odd factor as the largest, or the initial n if no other factors
    return factor if factor == n or factor % 2 == 0 else n