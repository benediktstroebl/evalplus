def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    factor = n
    while factor % 2 == 0:
        factor //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while factor % i == 0:
            factor //= i
    if factor > 1:
        return factor
    else:
        return n