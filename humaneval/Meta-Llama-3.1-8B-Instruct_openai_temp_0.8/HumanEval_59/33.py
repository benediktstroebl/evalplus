```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. 
    Assume n > 1 and is not a prime.

    Args:
        n (int): A number greater than 1.

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

This script uses a simple trial division method to find the largest prime factor of a given number `n`. It iteratively divides `n` by the smallest prime factor `i` until it is no longer divisible. This process is repeated until `i` is greater than the square root of `n`. At this point, `n` is guaranteed to be a prime number, and it is returned as the largest prime factor.