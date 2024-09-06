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

The function iterates through potential factors from 2 up to the square root of `n` (skipping odd numbers). It divides `n` by each even factor until it is reduced to 1. Thus, the largest prime factor is delivered. This method is efficient due to its focus on even factors, eliminating odd ones efficiently.