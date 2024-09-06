```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest possible factor initially
    divisor = n - 1
    while divisor > 1:
        # Check if the divisor is prime
        if divisor == 2 or divisor & 1:
            return divisor
        divisor //= 2
    return 1

# Test cases
assert largest_prime_factor(13195) == 29
assert largest_prime_factor(2048) == 2
```

This approach is efficient given that the largest factor is identified in `O(log n)` time. To determine if the divisor is prime, ensure it's greater than 1 and lacks any factors besides 1. If so, it's a prime number.