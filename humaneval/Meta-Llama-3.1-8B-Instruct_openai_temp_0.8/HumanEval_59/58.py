```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
    n (int): A positive integer greater than 1 that is not prime.
    
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

This function works by continuously dividing the input number `n` by the smallest prime number (2) as long as `n` is divisible by it. If `n` is not divisible by 2, the function increments the divisor `i` by 1. This process continues until `i` squared is greater than `n`. At this point, `n` will be a prime number and the function returns it as the largest prime factor.