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
    return n
```
The function iterates through potential factors from 2 up to the square root of `n` (inclusive), dividing `n` by any factor it finds. It starts the search from 3 as any factor greater than 2 would already have been found in the initial `2` iteration. This approach ensures that `n` is divided only by prime numbers, resulting in the largest prime factor being assigned to `factor`. In the end, if `factor` is greater than 1, it is returned as the largest prime factor; otherwise, `n` is returned, assuming it to be a prime number. This approach efficiently solves the problem in a single function, without introducing unnecessary complexity.