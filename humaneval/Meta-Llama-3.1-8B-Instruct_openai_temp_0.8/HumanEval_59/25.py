```python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
    n (int): The input number.

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

# Example usage
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script works by continuously dividing the input number `n` by the smallest prime number `i` until `n` is no longer divisible by `i`. At this point, `n` is the largest prime factor of the original number.