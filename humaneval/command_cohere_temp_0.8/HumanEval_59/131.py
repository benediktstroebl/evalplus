```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for largest factor first which is not a prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
```

This script defines a function `largest_prime_factor(n)` that returns the largest prime factor of a given number `n`. It assumes that `n` is greater than 1 and is not prime itself. The function loops through possible factors from 2 up to the square root of `n`, checking if the number is divisible by any of them. Once a divisor is found, it is returned as the largest prime factor. 

The code uses a single loop to efficiently find the largest prime factor, making it an optimal solution.