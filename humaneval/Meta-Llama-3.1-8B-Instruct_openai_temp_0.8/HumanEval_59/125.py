```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): A composite number.

    Returns:
    int: The largest prime factor of n.

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

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. The function works by dividing `n` by increasing integers until it finds a divisor. If the current divisor is not a divisor of `n`, it increments the divisor. If the divisor is a divisor of `n`, it divides `n` by the divisor. This process continues until `n` is reduced to its largest prime factor. The function finally returns this largest prime factor.