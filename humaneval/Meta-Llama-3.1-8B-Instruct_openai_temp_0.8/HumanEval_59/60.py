```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    This function works by dividing n by the smallest prime number (2) as long as it's divisible, 
    then moving on to the next number (3) and so on, until we find a prime factor.
    
    Args:
        n (int): A number greater than 1 that is not a prime.
    
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

This script uses a while loop to check for divisibility by the smallest possible prime number (2) as long as it's divisible, and then increments to the next number (3). This continues until it finds a prime factor. If a prime factor is found, it keeps dividing n by this factor until it's no longer divisible. At this point, n is a prime number and is the largest prime factor of the original number.