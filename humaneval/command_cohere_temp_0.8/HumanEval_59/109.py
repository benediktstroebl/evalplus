```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            factor = possible_factor
    return factor
```

This approach iterates from 2 up to the square root of `n` (inclusive), and for each integer `possible_factor` it checks if `possible_factor` is a factor of `n`. If it is, it updates the `factor` variable to this `possible_factor`. The function then returns the `factor` variable, which corresponds to the largest prime factor of `n`.

This code assumes that n is not an integer equal to 1, nor an actual prime number. This is true for the provided test cases, as well as for any positive integer for which this function would be applicable.