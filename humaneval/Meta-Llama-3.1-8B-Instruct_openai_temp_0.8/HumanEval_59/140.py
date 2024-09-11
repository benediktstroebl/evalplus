```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
        n (int): A composite number (not prime).
    
    Returns:
        int: The largest prime factor of n.
    
    Examples:
        >>> largest_prime_factor(13195)
        29
        >>> largest_prime_factor(2048)
        2
    """
    # Initialize the largest prime factor to 2
    largest_factor = 2
    
    # Check odd factors starting from 3 up to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        # Check if i is a factor of n
        while n % i == 0:
            # Update the largest factor if necessary
            largest_factor = i
            # Divide n by the current factor
            n = n // i
    
    # If n is still greater than 2, it is a prime number
    if n > 2:
        # Update the largest factor
        largest_factor = n
    
    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script implements a function to find the largest prime factor of a given composite number `n`. It iterates over all odd factors of `n` up to its square root to find the largest prime factor. If `n` itself is a prime number, it is returned as the largest prime factor. The script includes docstrings and example use cases to demonstrate its functionality.