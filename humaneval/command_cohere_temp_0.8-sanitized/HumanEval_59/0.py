def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Divide n by 2 until odd, then multiply by 2^(ceil(log2(n)) - 2)
    # The largest prime factor of n will be 2, if not divisible by 2
    while n % 2 == 0:
        n //= 2
    # Start from 3 to skip 2 and divide by 2 until it's exhausted
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            n //= i
    return n