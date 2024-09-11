```python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
    n (int): A positive integer greater than 1.
    
    Returns:
    int: The largest prime factor of n.
    
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

# Example usage
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
This script implements the trial division method to find the largest prime factor of a given number. It iteratively divides the input number `n` by the smallest prime factor (starting from 2), until it is no longer divisible. The last remaining number is the largest prime factor. The script demonstrates this with two example inputs, `13195` and `2048`.