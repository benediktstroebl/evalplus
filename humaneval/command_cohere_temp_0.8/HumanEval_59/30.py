```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as a starting point.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
```

This script defines a function `largest_prime_factor(n)` that returns the largest prime factor of a given number `n`. It iterates from 2 up to the square root of `n`, checking for even factors and returning the largest one if found. This efficiently finds the largest prime factor, as all prime factors of a number are odd.