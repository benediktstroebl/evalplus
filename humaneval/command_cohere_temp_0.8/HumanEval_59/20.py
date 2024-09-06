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

The function iterates through potential factors from 2 up to the square root of `n` (skipping odd numbers). It factors out all even factors starting from 2. It then takes steps of 2 in increasing odd numbers (`3, 5, 7`, etc.) and factors out all multiples of these odd factors. The final factor left, if greater than 1, will be the largest prime factor. This approach avoids unnecessary factoring of primes and efficiently identifies the largest prime factor.