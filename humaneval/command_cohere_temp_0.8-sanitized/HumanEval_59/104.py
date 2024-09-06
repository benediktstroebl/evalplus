def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest possible factor
    max_factor = n - 1
    while max_factor % 2 == 0:
        max_factor //= 2
    for possible_factor in range(3, int(n ** 0.5) + 1, 2):
        while n % possible_factor == 0:
            n //= possible_factor
            if n == 1:
                return possible_factor
    return n