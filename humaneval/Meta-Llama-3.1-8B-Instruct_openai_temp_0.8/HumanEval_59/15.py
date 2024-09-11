```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    :param n: A positive integer.
    :return: The largest prime factor of n.
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

This script works by dividing `n` by increasing integers until we find a factor. If the current integer `i` is not a factor of `n`, we try the next integer. If `i` is a factor, we continue dividing `n` by `i` until `n` is no longer divisible by `i`. At this point, `n` is the largest prime factor of the original number.