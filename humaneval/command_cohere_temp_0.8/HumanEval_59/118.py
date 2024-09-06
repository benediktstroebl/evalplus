```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Filter out non-prime factors and return the largest one.
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            n //= i
        if n == 1:
            return i
    return n
```