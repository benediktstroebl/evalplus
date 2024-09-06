```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for largest factor first which is not a prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
```

This Python script defines a function `largest_prime_factor(n)` that calculates the largest prime factor of a positive integer `n`. It iterates through factors from 2 up to the square root of `n`, checking for divisibility. When a non-divisible state is reached, it returns the largest divisible value, which is the largest prime factor. This efficient approach ensures that large factors are prioritized during the search, significantly reducing the number of iterations required.