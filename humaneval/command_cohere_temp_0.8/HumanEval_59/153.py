```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    def is_prime(m):
        """Check if m is a prime number."""
        if m < 2:
            return False
        for i in range(2, int(m ** 0.5) + 1):
            if m % i == 0:
                return False
        return True

    # Traverse through 2 and sqrt(n) to find the largest prime factor
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and is_prime(i):
            return i
    # If no factors are found, then n is a prime itself
    return n
```