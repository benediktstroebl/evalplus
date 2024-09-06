def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def count_up_to(n):
    """Return an array of the first n prime numbers less than n."""
    result = []
    for i in range(2, n + 1):
        if is_prime(i) and i < n:
            result.append(i)
    return result