def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Write n as 2^a * 3^b * 5^c * ... * p_k^z with a > 0, b >= 0, c >= 0, ...
    # and z >= 1. (There may be fewer terms.)
    # The largest factor must involve the largest a, so largest factor
    # is 2^a.
    for power in range(30, 0, -1):
        if n > 2 ** power:
            n //= 2 ** power
            a += power
    return 2 ** a if n == 1 else -1