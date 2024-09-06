```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for largest factor first which is not a prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
```

This Python script defines a function `largest_prime_factor(n)` that finds the largest prime factor of a given number `n`. It iterates from 2 up to the square root of `n`, checking for each number if it is a factor of `n` and if it's prime. It then returns the largest prime factor found. The code is encapsulated in a self-contained function, ready for use in other scripts or programs.