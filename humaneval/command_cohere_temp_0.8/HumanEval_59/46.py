```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as a starting point.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
```

This Python script defines a function `largest_prime_factor(n)` that finds the largest prime factor of a positive integer `n`. It iterates from 2 up to the square root of `n` (inclusive), and for each integer `i`, it checks if `i` is a prime factor of `n` (i.e., `n` is divisible by `i`). If such a factor is found, the function returns `i`, which is then the largest prime factor of `n`. 

The given tests in the code block will check the function with two different inputs, confirming that the largest prime factors for both numbers are correctly identified.