```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as a starting point.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
```

This Python script defines a function `largest_prime_factor(n)` that calculates the largest prime factor of a positive integer `n`. It iterates from 2 up to the square root of `n`, checking for divisibility. When `n` is divisible by an integer `i`, it returns that `i` as the largest prime factor. This efficient approach ensures that non-prime factors are eliminated, ultimately leading to the largest prime factor.