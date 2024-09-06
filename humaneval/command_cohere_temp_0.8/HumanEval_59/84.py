```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as the largest prime factor
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
```

This code defines a function `largest_prime_factor(n)` that finds the largest prime factor of a positive integer `n`. It iterates from 2 up to the square root of `n` (inclusive). For each number `i`, it checks if `i` is a prime factor of `n` (i.e., `n % i == 0`). If such a factor is found, the function returns `i` as the largest prime factor. This strategy ensures that the largest even factor is chosen as the largest prime factor, as it's assumed that `n` is not an prime itself. 

The function is designed to handle positive integers only, and it assumes that `n` is not an prime itself (i.e., `n > 1`).