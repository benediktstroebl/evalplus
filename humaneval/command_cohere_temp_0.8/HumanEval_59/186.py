```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for largest factor first which is not a prime
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
```

This code defines a Python function called `largest_prime_factor` that takes a single argument `n`, representing a positive integer. This function iterates through factors from 2 up to the square root of `n`, checking if `n` is divisible by each factor. If a factor divides `n` without leaving a remainder, it means that factor is the largest prime factor of `n`. The function returns this largest prime factor. 

The iterative approach ensures efficiency in factoring large integers, as it eliminates the need for repeated divisions. This function is straightforward and effectively determines the largest prime factor of any given positive integer `n`.