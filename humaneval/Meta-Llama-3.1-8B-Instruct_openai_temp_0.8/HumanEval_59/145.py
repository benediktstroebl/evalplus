```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
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

This script defines a function `largest_prime_factor` that finds the largest prime factor of a given number `n`. It uses a while loop to divide `n` by the smallest prime factor (which is 2) as long as it's divisible. Then it increments the divisor until it finds the next number that can divide `n`, which will be a prime factor. This process is repeated until `n` is reduced to its largest prime factor.