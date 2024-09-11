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

This script uses a simple algorithm to find the largest prime factor of a given number. It starts from 2 and divides the number by the current number as long as it's divisible. If it's not divisible, it increments the current number by 1. This process continues until the current number squared is greater than the number. The remaining number is the largest prime factor.