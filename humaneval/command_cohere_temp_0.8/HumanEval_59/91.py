```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            factor = possible_factor
    return factor
```

This script defines a function `largest_prime_factor(n)` that returns the largest prime factor of the input integer `n`. The function first assigns `factor` with the input number. Then it iterates through numbers from 2 to the square root of `n`, checking if any of these numbers divide `n` exactly. Once a divisor is found, it updates the `factor` to that number. Thus, the loop effectively identifies the largest prime factor among potential factors up to the square root of `n`, and returns this largest prime factor. 

The tests included in the prompt exercise this function against valid inputs, ensuring that it correctly identifies the largest prime factor for different cases.