def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            factor = possible_factor
    # Check for potential factors greater than int(n**0.5) as well
    # Note: The condition `possible_factor * possible_factor > n`
    # ensures that we only consider squares of numbers whose square
    # is less than or equal to n.
    for possible_factor in range(int(n**0.5) + 1, n):
        if n % possible_factor == 0 and possible_factor * possible_factor <= n:
            factor = possible_factor
    return factor