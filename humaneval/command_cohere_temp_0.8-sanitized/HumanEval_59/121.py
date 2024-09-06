def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Go through each number from 2 to n, and see if it's a factor, noting the largest one
    largest_factor = n
    for num in range(2, n + 1):
        if n % num == 0:
            largest_factor = max(largest_factor, num)
    return largest_factor