```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
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

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that calculates the largest prime factor of a given number `n`. It works by dividing `n` by increasing integers `i` until `i` is no longer a factor of `n`. The process stops when `i` is greater than the square root of `n`, because a larger factor of `n` would be a multiple of a smaller factor that has already been accounted for. The function returns the last remaining factor, which is the largest prime factor of `n`.