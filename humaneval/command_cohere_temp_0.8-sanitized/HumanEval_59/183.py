def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Breadth-first search for factors
    i, factor = 2, n
    while i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factor = max(factor, i)
    return factor