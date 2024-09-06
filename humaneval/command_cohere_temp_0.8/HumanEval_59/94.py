```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as a starting point.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
```

This Python script defines a function `largest_prime_factor(n)` that finds the largest prime factor of a positive integer `n`. It iterates from 2 up to the square root of `n` (inclusive), and for each integer `i`, it checks if `i` is a factor of `n` (i.e., `n % i == 0`). If `i` is a factor, it returns `i` as the largest prime factor. The loop is optimized to check only up to the square root, as any larger factor would have a corresponding factor smaller than the square root.