```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as a starting point.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
```

This function loops through possible factors from 2 up to the square root of `n`, checking for even factors and factoring out `i` if it is a divisor of `n`. This works because larger prime factors are typically toward the beginning of the factorization sequence. This approach helps optimize the search for the largest prime factor.