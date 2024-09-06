```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest odd factor
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
    # If all factors are even, return the largest even factor
    return 2
```