def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Handle the case of n being a power of 2, which has no digits after the decimal point
    if n == 2:
        return 2
    while n % 2 == 0:
        n //= 2
    # The following loop handles cases of n having digits after the decimal point
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            n //= i
    return n