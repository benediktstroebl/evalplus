### Largest Prime Factor Script
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): An integer greater than 1.

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
print(largest_prime_factor(13195))  # Expected output: 29
print(largest_prime_factor(2048))   # Expected output: 2
```

This script defines a function `largest_prime_factor(n)` that finds the largest prime factor of a given integer `n`. It does this by dividing `n` by the smallest prime factor (2) and continuing to divide by the smallest prime factor until `n` is no longer divisible by it. The process is repeated with increasing integers (potential prime factors) until the square of the potential prime factor is greater than `n`. At this point, `n` itself is the largest prime factor.