```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): A composite number greater than 1.

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

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor(n)` that returns the largest prime factor of `n`. The algorithm works by dividing `n` by the smallest divisor (which is 2) as long as it's divisible. Then it increments the divisor until it finds the next one that can divide `n`, which will be a prime number. This process continues until `i * i` is greater than `n`, at which point `n` will be a prime number. In this case, `n` itself is the largest prime factor.