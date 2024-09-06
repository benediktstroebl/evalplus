def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Loop through each number from 2 to the square root of n.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i