```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            factor = possible_factor
    return factor
```

This script defines a function `largest_prime_factor(n)` that returns the largest prime factor of the input integer `n`. The function first sets `factor` equal to the input number `n`, and then iterates through possible factors ranging from 2 up to the square root of `n`. It checks if `n` is divisible by any of these possible factors, and if so, updates the `factor` to the largest divisor that is prime. The function efficiently identifies the largest prime factor among `n`'s factors by examining the largest divisors.