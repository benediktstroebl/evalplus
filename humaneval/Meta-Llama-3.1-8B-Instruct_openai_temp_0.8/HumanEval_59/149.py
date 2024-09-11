```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
    n (int): A positive integer greater than 1.

    Returns:
    int: The largest prime factor of n.
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Test cases
print(largest_prime_factor(13195))  # Expected: 29
print(largest_prime_factor(2048))   # Expected: 2
```

This script defines a function `largest_prime_factor(n)` that takes an integer `n` as input and returns its largest prime factor. The function works by dividing `n` by the smallest prime factor (2) as long as it's divisible, then incrementing the divisor until it finds the next number that can divide `n`. This process repeats until `n` is reduced to its largest prime factor. The function includes docstrings to provide information about its arguments and return values, as well as test cases to verify its correctness.