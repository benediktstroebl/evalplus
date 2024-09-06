def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for largest factor first
    largest = n // 2
    while largest > 1 and not is_prime(largest):
        largest //= 2
    if largest > 1:
        return largest
    # If not, then check from the square root
    sqrt = int(n ** 0.5)
    for i in range(sqrt, 1, -1):
        if is_prime(i):
            return i
def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True