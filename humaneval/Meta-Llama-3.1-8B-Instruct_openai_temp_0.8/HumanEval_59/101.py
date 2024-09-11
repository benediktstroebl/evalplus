```python
def largest_prime_factor(n: int) -> int:
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

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script works by dividing `n` by the smallest prime factor (`i`) until `n` is no longer divisible by `i`. It then increments `i` and continues the process until `n` is reduced to its largest prime factor. 

This is done efficiently by only checking up to the square root of `n`, as a larger factor of `n` must be a multiple of a smaller factor that has already been checked.