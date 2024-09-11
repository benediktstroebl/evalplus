```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

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

This script works by dividing the input number `n` by the smallest prime factor (2) as long as it's divisible. Then it increments the divisor `i` by 1 and checks if `n` is divisible by `i`. If it is, it replaces `n` with `n // i` to continue the process with the new value of `n`. This process repeats until `n` is no longer divisible by `i`. At this point, `n` is the largest prime factor of the original `n`.