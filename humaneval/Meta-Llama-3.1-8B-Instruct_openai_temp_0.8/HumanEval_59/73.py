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

This script uses a simple algorithm to find the largest prime factor of a given number. It works by dividing the number by increasing integers, starting from 2, until it finds a factor. It keeps track of the largest factor found so far and returns it at the end. If the number is a prime, it returns the number itself.