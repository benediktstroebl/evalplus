def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            factor = possible_factor
    # Check for odd factors causing initial factor to be overestimated
    if n % 2 == 0:
        if factor % 2 == 0:
            factor -= 1
    return factor