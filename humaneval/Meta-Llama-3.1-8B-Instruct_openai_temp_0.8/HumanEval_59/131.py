```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Parameters:
    n (int): The number to find the largest prime factor of.

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

This script defines a function `largest_prime_factor` that takes an integer `n` and returns its largest prime factor. It does this by dividing `n` by the smallest prime number (2) as long as it's divisible, then increments the divisor until it finds the next number that `n` is divisible by. It continues this process until `n` is no longer divisible by any number less than or equal to its square root, at which point `n` itself is the largest prime factor.