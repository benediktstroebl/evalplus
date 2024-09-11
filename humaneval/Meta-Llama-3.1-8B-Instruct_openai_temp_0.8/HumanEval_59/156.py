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
    # Initialize the largest factor to 1
    largest_factor = 1
    
    # Start dividing from 2, the smallest prime number
    i = 2
    
    # Continue dividing until we reach the square root of n
    while i * i <= n:
        # If n is divisible by i, then i is a factor of n
        if n % i:
            # If i is not a factor, increment it by 1
            i += 1
        else:
            # If i is a factor, update the largest factor
            largest_factor = i
            # Divide n by i to remove the factor
            n = n // i
    
    # If n is not 1 at this point, it means n itself is a prime number
    if n > 1:
        # In that case, n is the largest prime factor
        largest_factor = n
    
    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script works by iteratively dividing `n` by the smallest divisor `i` until `n` is no longer divisible by `i`. It keeps track of the largest factor found so far and updates it whenever a larger factor is found. Finally, if `n` is not 1 at the end, it means `n` itself is a prime number, so it is returned as the largest prime factor.