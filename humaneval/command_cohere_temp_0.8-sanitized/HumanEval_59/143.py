def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            factor = possible_factor
    # Check for potential factors greater than int(n**0.5) as well
    # Note: This section is slower but is unlikely to make a difference
    # for typical inputs. See https://en.wikipedia.org/wiki/Prime_number#Prime_numbers_less_than_political_powers_of_two
    if factor == n:
        for possible_factor in range(3, int(n**0.5) + 1, 2):
            if n % possible_factor == 0:
                factor = possible_factor
    return factor