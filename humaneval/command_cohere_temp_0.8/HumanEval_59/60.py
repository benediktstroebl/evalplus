```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Traverse through 2, 3, ..., floor(n/2)
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return i
```