def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Go through each number from 2 to n, and check if n is divisible, starting from the end.
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            return i