```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): The input number.

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

This script uses a simple approach to find the largest prime factor of a given number. It starts by dividing the number by 2, and then it checks for the next odd number (since all prime numbers are of the form 6n ± 1, where n is any integer) to find the largest prime factor. The loop continues until the number is reduced to 1. The last remaining number will be the largest prime factor.