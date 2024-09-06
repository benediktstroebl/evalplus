def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for largest factor first
    largest = n // 2
    while largest % 2 == 0:
        largest //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while largest % i == 0:
            largest //= i
    if largest > 1:
        return largest
    return n