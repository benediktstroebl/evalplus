def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Write n as 2^a * b, where b is odd
    a, b = 0, n
    while b % 2 == 0:
        a += 1
        b //= 2
    # b is odd at this point
    # Let c be the largest factor of b
    for c in range(3, int(b**0.5) + 1, 2):
        while b % c == 0:
            b //= c
        if b == 1:
            return c * (2**a)
    return b