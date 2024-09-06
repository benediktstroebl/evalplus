def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            factor = possible_factor
    # Check for divisibility by odd numbers greater than int(n**0.5) as well
    # This is necessary because n could be a decimal number like 27.3
    for possible_factor in range(3, int(n**0.5) + 2):
        if n % possible_factor == 0:
            factor = possible_factor
    return factor