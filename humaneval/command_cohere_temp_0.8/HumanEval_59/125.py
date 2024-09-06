```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            factor = possible_factor
    # Check for n being a prime number
    if factor == n:
        return n
    return factor
```
The function iterates through possible factors from 2 up to `int(n**0.5) + 1` (which is the square root of `n` plus 1). If a factor is found, it updates the `factor` variable to this value. Once the loop completes, it checks if `factor` is equal to `n`. If so, `n` is a prime number, if not, `factor` holds the largest prime factor.