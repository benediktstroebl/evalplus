```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): A positive integer greater than 1.

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

This script defines a function `largest_prime_factor(n)` that finds the largest prime factor of a given positive integer `n`. It uses a while loop to check divisibility from 2 to sqrt(n), and updates the value of `n` by dividing it by the current divisor until it is no longer divisible. The remaining value of `n` is the largest prime factor. The script then tests this function with the provided examples.