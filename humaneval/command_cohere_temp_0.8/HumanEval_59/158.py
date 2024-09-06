```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    while factor % 2 == 0:
        factor //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while factor % i == 0:
            factor //= i
    if factor > 1:
        return factor
```

The function iterates through potential factors from 2 up to `n ** 0.5` (prevents potential overflow issues). It factors out multiples of 2 and then moves through potential factors in increments of 2 (much faster than iterating through numbers sequentially). The loop will eventually encounter the largest prime factor, and if after the loops there's a factor greater than 1, that's the largest prime factor.