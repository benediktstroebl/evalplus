def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Check for edge cases: 2 and 5
    if n == 2 or n == 5:
        return n
    # Divide n by 2, 3, 5, 7, 11, ...
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            n //= i
    # If n is still greater than 1, it is a prime
    if n > 1:
        return n
    # Otherwise, n must be 1
    return 1