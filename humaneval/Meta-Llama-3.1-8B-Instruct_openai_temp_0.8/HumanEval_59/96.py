```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): The input number.

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

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script works by dividing `n` by increasing integers `i` until it finds a divisor. Once a divisor `i` is found, `n` is divided by `i` in each iteration. This process continues until `n` is reduced to its largest prime factor. The while loop ends when `i` squared is greater than `n`, because a larger factor of `n` would be a multiple of a smaller factor that has already been accounted for.