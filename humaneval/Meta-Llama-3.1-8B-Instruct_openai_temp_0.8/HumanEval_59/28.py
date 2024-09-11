```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): An integer greater than 1.

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
if __name__ == "__main__":
    print(largest_prime_factor(13195))   # Output: 29
    print(largest_prime_factor(2048))    # Output: 2
```

This script works by continuously dividing `n` by the smallest divisor `i` until `n` can no longer be divided. At that point, `n` will be the largest prime factor of the original number.