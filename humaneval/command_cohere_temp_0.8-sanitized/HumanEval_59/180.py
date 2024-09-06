def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Infinitely iterates through prime factors, starting from 2
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            n //= i
        else:
            return i
    return n