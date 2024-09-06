def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Check for the edge case where n is a power of 2, which has no prime factors other than 2
    if n == 2:
        return 2
    while n % 2 == 0:
        n //= 2
    # The prime factorization of n must have at least one odd factor
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            n //= i
    if n > 2:
        return n
    return 2