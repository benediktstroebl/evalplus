```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

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

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. The function uses a trial division approach to find the largest prime factor. It starts by dividing `n` by the smallest prime number, 2, and continues dividing by increasing integers until the square root of `n` is reached. If `n` is divisible by an integer `i`, it is divided by `i`, otherwise `i` is incremented. The process continues until `n` is no longer divisible by any integer, at which point `n` is the largest prime factor.