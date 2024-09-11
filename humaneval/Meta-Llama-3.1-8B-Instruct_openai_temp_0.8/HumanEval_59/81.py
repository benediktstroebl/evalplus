```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
    n: An integer greater than 1 and not a prime number.
    
    Returns:
    The largest prime factor of n.
    
    Examples:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    
    # Initialize the largest factor to 1
    largest_factor = 1
    
    # Start checking from 2 (the smallest prime number)
    i = 2
    
    # Continue until we find a factor or i reaches the square root of n
    while i * i <= n:
        # If n is divisible by i, it means i is a factor of n
        if n % i:
            # If n is not divisible by i, increment i by 1
            i += 1
        else:
            # If n is divisible by i, update the largest factor and divide n by i
            largest_factor = i
            n //= i
    
    # If n is not 1 at this point, it means n is a prime number
    if n > 1:
        # Update the largest factor to n
        largest_factor = n
    
    # Return the largest prime factor
    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))  # Output: 2
```

This script defines a function `largest_prime_factor(n)` that takes an integer `n` as input and returns its largest prime factor. It uses a loop to iterate over all numbers from 2 to the square root of `n`, checking if each number is a factor of `n`. If a factor is found, it is updated as the largest factor and `n` is divided by this factor. The process continues until all factors have been found. If `n` is a prime number, it is returned as the largest factor. The function is tested with two examples: `13195` and `2048`.