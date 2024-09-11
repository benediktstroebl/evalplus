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

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script uses a simple trial division approach to find the largest prime factor of a given number. It starts by checking divisibility from 2 and increments the divisor until it finds a number that can divide the input without leaving a remainder. It continues this process until `n` is reduced to a prime number, which is the largest prime factor of the original `n`.