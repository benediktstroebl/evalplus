```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
        n (int): A composite integer (not prime).
    
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
print(largest_prime_factor(13195))  # 29
print(largest_prime_factor(2048))   # 2
```

This script uses a simple trial division method to find the largest prime factor of `n`. It starts dividing `n` by `i` (initially set to 2) as long as `n` is divisible by `i`. If `n` is not divisible by `i`, it increments `i`. This process continues until `i` is greater than the square root of `n`, at which point `n` is guaranteed to be prime, and the function returns `n`.