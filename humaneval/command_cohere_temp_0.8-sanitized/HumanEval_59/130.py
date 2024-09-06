def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for largest factor first
    largest = n // 2
    while largest > 1 and not prime(largest):
        largest //= 2
    if largest > 1:
        return largest
    # If not, then must be a composite of 2 and an odd factor
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
def prime(n):
    """Check if n is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True