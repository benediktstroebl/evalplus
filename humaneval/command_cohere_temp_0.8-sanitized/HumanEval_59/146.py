def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    while factor > 1:
        test = 2
        while test ** 2 <= factor:
            test += 1
        if factor == test - 1:
            break
        elif factor % test == 0:
            factor //= test
        else:
            test += 1
    return factor