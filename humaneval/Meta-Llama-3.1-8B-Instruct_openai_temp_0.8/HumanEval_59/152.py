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
    
    # Initialize the largest factor to 1
    largest_factor = 1
    
    # Start checking from 2, the smallest prime number
    i = 2
    
    # Continue checking until n is reduced to 1
    while n > 1:
        # If n is divisible by i, update largest_factor and divide n by i
        if n % i == 0:
            largest_factor = i
            n = n // i
        # If n is not divisible by i, increment i
        else:
            i += 1
    
    # Return the largest prime factor found
    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that finds the largest prime factor of a given number `n`. It iterates through all numbers from 2 to `n` and checks if `n` is divisible by the current number. If it is, it updates the `largest_factor` and divides `n` by the current number. If `n` is not divisible by the current number, it increments the current number. The function continues this process until `n` is reduced to 1, at which point it returns the `largest_factor`, which is the largest prime factor of `n`.