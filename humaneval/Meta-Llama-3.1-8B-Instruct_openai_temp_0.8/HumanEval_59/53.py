```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): A positive integer.

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

This script uses a simple trial division method to find the largest prime factor of a given number `n`. It starts from 2 and checks if `n` is divisible by the current number `i`. If it is, it divides `n` by `i` and continues the loop. If `n` is not divisible by `i`, it increments `i` until the next number that can divide `n` is found, which will be `n` itself. At that point, the largest prime factor of `n` is returned.