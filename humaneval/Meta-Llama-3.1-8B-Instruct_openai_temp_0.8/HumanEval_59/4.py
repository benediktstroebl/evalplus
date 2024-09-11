```python
def largest_prime_factor(n: int):
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

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script works by dividing `n` by the smallest prime number, which is 2, as long as `n` is divisible by 2. Then it increments the divisor to the next number and checks if `n` is divisible by it. This process continues until `n` is no longer divisible by any number (i.e., it becomes a prime number). The last divisor that divided `n` is the largest prime factor of `n`.