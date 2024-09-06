def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Special case: n is a power of 2, which has no digits after the decimal point
    if n == 2:
        return 2
    while n % 2 == 0:
        n //= 2
    # From here on, n is odd, so only single digits matter for primality
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            n //= i
    return n