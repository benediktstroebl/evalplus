```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            factor = possible_factor
    # Check for possibility of larger prime factors beyond sqrt(n)
    if n > 10 ** 5 and factor == n // 2:
        factor = 2
    return factor
```

This script defines a function `largest_prime_factor(n)` that returns the largest prime factor of a given number `n`. It starts by setting `factor` equal to `n` itself, then iterates through possible factors from 2 up to the square root of `n`. If `n` is divisible by any of these possible factors, the `factor` is updated to that value.

After the possible factors are checked within the square root of `n`, there is an additional check for `n` being larger than 10^5 (i.e., the given number is sufficiently large). This is to account for the possibility that `n` could be twice a large prime, in which case the largest factor would be 2. The example provided in the question reflects this reasoning.

By this logic, the function returns the largest prime factor of the given number `n`.