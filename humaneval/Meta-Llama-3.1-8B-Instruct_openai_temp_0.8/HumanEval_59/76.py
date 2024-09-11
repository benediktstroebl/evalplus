```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): A positive integer greater than 1.

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

This script uses trial division to find the largest prime factor of a given number `n`. It starts by dividing `n` by the smallest prime number, 2, and continues dividing by increasing integers until it finds a divisor. It then continues by dividing `n` by the next integer that is not a divisor, which is the next prime number. This process continues until `n` is reduced to a prime number, which is then returned as the largest prime factor.