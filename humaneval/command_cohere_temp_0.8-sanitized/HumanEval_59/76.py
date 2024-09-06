def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Greatest factorization algorithm
    largest_factor = n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            largest_factor = i
            while n % i == 0:
                n //= i
    if n > 1:
        largest_factor = n
    return largest_factor