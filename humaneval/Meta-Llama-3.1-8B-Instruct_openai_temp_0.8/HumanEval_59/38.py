```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    
    Parameters:
    n (int): A positive integer greater than 1 and not a prime number.
    
    Returns:
    int: The largest prime factor of n.

    Example:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Initialize the largest factor
    largest_factor = None
    
    # Iterate from the smallest prime number
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i is a factor of n
        while n % i == 0:
            # Update the largest factor
            largest_factor = i
            # Divide n by i
            n = n // i
    
    # If n is a prime number greater than 1, it will be the largest factor
    if n > 1:
        largest_factor = n
    
    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` and returns its largest prime factor. It iterates from the smallest prime number (2) to the square root of `n` and checks if each number is a factor of `n`. If a number `i` is a factor, it updates the largest factor and divides `n` by `i`. If `n` is a prime number greater than 1, it will be the largest factor. The function returns the largest prime factor. The example use cases are provided at the end of the script.