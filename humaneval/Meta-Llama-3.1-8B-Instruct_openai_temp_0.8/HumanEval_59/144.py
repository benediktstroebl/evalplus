```python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
        n (int): A positive integer greater than 1.
    
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
print(largest_prime_factor(600851475143))  # Output: 6857
```

This script defines a function `largest_prime_factor(n)` that takes an integer `n` as input and returns its largest prime factor. The function works by iteratively dividing `n` by the smallest prime factor (which is 2) as long as it is divisible. Then it increments the divisor until it finds the next number that can divide `n`, which will be a prime factor. This process continues until `n` is reduced to its largest prime factor.