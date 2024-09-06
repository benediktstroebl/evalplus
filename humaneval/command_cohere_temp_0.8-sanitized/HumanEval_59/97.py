def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            factor = possible_factor
    # Check for possible factors greater than int(n**0.5) as well
    # The above loop handles all smaller factors
    while factor**2 <= n:
        factor += 1
    return factor