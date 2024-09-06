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

The function iterates through potential factors from 2 up to the square root of `n` (excluding `n` itself, since it's assumed to be larger than 2). It divides `n` by each even factor and then each odd factor. This approach allows detecting the largest prime factor.

We omit the type annotation for `n` to make the function more generic, although it still works for the intended case of integer input. This version is also more efficient, completing the same task in just one pass through the factors, thanks to the factorization step.

This approach significantly reduces the number of iterations required to find the largest prime factor. In the worst-case scenario, it will only iterate up to the square root of `n`, whereas the previous approach required iterations up to `n`.