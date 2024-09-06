```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for largest factor first
    largest = n // 2
    while largest % 2 == 0:
        largest //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while largest % i == 0:
            largest //= i
    if largest > 1:
        return largest
    return n
```

The provided solution iterates through potential prime factors from `3` up to `sqrt(n)`. It eliminates any even factors first by dividing `n` by 2 until it is odd. It then checks for divisibility by each odd potential prime factor, iterating through them by stepping `2`. This approach allows for a efficient elimination of potential factors.