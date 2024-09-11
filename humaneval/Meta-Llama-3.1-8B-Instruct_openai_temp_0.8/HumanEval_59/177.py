### Largest Prime Factor Function
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
        n (int): The number for which to find the largest prime factor.
    
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
print(largest_prime_factor(13195))  # Should print 29
print(largest_prime_factor(2048))   # Should print 2
```

This script defines a function `largest_prime_factor(n)` that calculates the largest prime factor of a given number `n`. It does this by continuously dividing `n` by the smallest prime number (2) as long as it's divisible, then moving on to the next number (in this case, `i += 1`). This continues until `n` is no longer divisible by any number up to its square root, at which point `n` itself is the largest prime factor.