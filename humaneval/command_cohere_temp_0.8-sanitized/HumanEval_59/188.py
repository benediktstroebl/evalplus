def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Check for highest value divisible by 2
    if n % 2 == 0:
        return 2
    # Check for highest value divisible by 3
    if n % 3 == 0:
        return 3
    # Check from 5 to square root of n
    for i in range(5, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
    # If no factors are found, return n
    return n