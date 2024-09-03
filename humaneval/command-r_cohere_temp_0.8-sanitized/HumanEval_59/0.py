def largest_prime_factor(n: int):
    """Return the largest prime factor of n > 1 which is not a prime."""
    if n % 2 == 0:
        return 2
    # Use the fact that all odd numbers greater than 2 can be written as 6k ± 1
    for k in range(1, (n - 1) // 3 + 1):
        if n % (6 * k) == 1:
            return 6 * k - 1
        elif n % (6 * k) == 5:
            return 6 * k + 1
    return None