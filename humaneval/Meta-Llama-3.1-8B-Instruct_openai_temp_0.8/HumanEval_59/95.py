```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n.
    
    Assume n > 1 and is not a prime.
    
    Parameters:
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
print(largest_prime_factor(13195))
print(largest_prime_factor(2048))
```

This script iterates from 2 to the square root of the input number `n`, checks for divisibility, and divides `n` if it's divisible. The remaining number after the loop is the largest prime factor of `n`.