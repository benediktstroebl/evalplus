```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): Input number.

    Returns:
    int: The largest prime factor of n.

    Example:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Initialize the largest factor as 2 (smallest prime number)
    largest_factor = 2
    
    # Iterate from 2 to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i is a factor of n
        while n % i == 0:
            # Update the largest factor
            largest_factor = max(largest_factor, i)
            # Divide n by i
            n = n // i
    
    # If n is a prime number greater than 2
    if n > 2:
        # Update the largest factor
        largest_factor = max(largest_factor, n)
    
    return largest_factor

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor(n)` that takes an integer `n` as input and returns the largest prime factor of `n`. It first initializes the largest factor as 2 (smallest prime number) and then iterates from 2 to the square root of `n` to find all the factors of `n`. The largest factor is updated accordingly. If `n` is a prime number greater than 2, the function updates the largest factor to `n`. Finally, the function returns the largest prime factor. The test cases at the end demonstrate the correctness of the function.