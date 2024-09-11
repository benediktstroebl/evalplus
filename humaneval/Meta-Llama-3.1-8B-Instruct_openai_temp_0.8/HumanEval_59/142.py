```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): A number greater than 1.

    Returns:
        int: The largest prime factor of n.

    Examples:
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

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor(n)` that takes an integer `n` as input and returns its largest prime factor. The function works by iterating from 2 to the square root of `n` and checking for divisibility. If `n` is divisible by `i`, it divides `n` by `i` and continues checking the remaining `n`. This process continues until `n` can no longer be divided by any number less than or equal to its square root, at which point `n` itself is the largest prime factor.

The script includes docstrings to provide documentation for the function, including a description, arguments, return values, and examples. It also includes test cases to verify the correctness of the function.