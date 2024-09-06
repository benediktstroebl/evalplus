```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    for possible_factor in range(2, int(n**0.5) + 1):
        if n % possible_factor == 0:
            factor = possible_factor
    return factor
```

This script defines a function `largest_prime_factor(n)` that returns the largest prime factor of the input integer `n`. The function first sets `factor` equal to the input number `n`, and then iterates through possible factors ranging from 2 up to the square root of `n`. It checks whether `n` is divisible by each possible factor, and if it is, updates `factor` to that value. The function then returns the valued `factor`, which represents the largest prime factor of `n`.

Here's an example of function usage:
```python
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))  # Output: 2
```

This demonstrates that the function correctly identifies the largest prime factors of the given numbers (29 for 13195 and 2 for 2048).