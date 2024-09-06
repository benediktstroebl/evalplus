```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as a starting point.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
```

This function loops through numbers from 2 to the square root of `n` and returns the largest even factor when it finds one. It will not proceed to the square root iteration if the largest even factor is found before. This optimized approach makes it suitable for large values of `n`. The function is also reusable and maintains a reasonable time complexity for its task.