def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # First, handle the case where n is a power of 2, which is the most common case.
    if n > 2 and (n & (n - 1)) == 0:  # checking if n is a power of 2
        return 2
    # Submit all numbers of the form i * 2^j, where i is an odd integer greater than 3
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return i