```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): A composite number.

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

This script defines a function `largest_prime_factor` that finds the largest prime factor of a given composite number `n`. It uses a while loop to divide `n` by the smallest divisor `i` until `n` is no longer divisible by `i`. The loop continues until `i` squared is greater than `n`, at which point `n` is guaranteed to be a prime number. The function then returns `n`, which is the largest prime factor of the original number.