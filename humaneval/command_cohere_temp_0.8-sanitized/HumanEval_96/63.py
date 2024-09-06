import unittest
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True
def count_up_to(n):
    """Return an array of the first n prime numbers less than n."""
    result = []
    for num in range(2, n + 1):
        if is_prime(num) and num < n:
            result.append(num)
    return result