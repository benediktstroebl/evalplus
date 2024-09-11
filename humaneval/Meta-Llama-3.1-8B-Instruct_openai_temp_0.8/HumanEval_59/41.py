```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    
    Args:
    n (int): The input number. Assume n > 1 and is not a prime.
    
    Returns:
    int: The largest prime factor of n.
    
    Examples:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    
    # Initialize the largest factor
    largest_factor = 2
    
    # Iterate from 2 to sqrt(n)
    for possible_factor in range(2, int(n**0.5) + 1):
        
        # While n is divisible by possible_factor, update largest_factor and divide n
        while n % possible_factor == 0:
            largest_factor = possible_factor
            n = n // possible_factor
    
    # If n is a prime number greater than 2, return n
    if n > 2:
        return n
    else:
        return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script uses a while loop to continuously divide the input number `n` by the possible factor `possible_factor` until `n` is no longer divisible by `possible_factor`. It keeps track of the largest factor found so far as it goes through the possible factors. If `n` is a prime number greater than 2, it returns `n` as the largest prime factor.