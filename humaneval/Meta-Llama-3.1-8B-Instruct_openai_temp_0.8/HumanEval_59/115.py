```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n.
    Assume n > 1 and is not a prime.

    Args:
    n (int): A number greater than 1 that is not a prime.

    Returns:
    int: The largest prime factor of n.

    Example:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. The function works by dividing `n` by the smallest prime number (2) as long as it's divisible, then increments the divisor until it finds the next number that can divide `n`, which will be a prime factor. This process continues until `n` is reduced to its largest prime factor.

The script includes docstrings to describe the function's purpose, parameters, return value, and example usage. Two test cases are included at the end to demonstrate the function's correctness.