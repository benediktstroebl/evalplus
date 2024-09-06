```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as a starting point.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
```

This Python script defines a function `largest_prime_factor(n)` that finds the largest prime factor of a positive integer `n`. It iterates from 2 up to the square root of `n` (inclusive), and for each integer `i`, it checks if `i` is a prime factor of `n` (i.e., `n % i == 0`). If it is, this `i` is returned as the result; otherwise, the loop continues until a prime factor is found. This efficiently finds the largest prime factor because it stops searching as soon as a prime factor is found, ensuring that all larger factors are also prime.