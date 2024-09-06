def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Quick lobe factors out all multiples of 2 from n
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            n //= i
    # n must be a prime at this point
    return n