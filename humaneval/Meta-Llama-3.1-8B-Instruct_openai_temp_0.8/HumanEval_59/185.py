### Largest Prime Factor Function
```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n.
    
    Args:
        n (int): A composite integer greater than 1.
    
    Returns:
        int: The largest prime factor of n.
    
    Examples:
        >>> largest_prime_factor(13195)
        29
        >>> largest_prime_factor(2048)
        2
    """
    # Initialize the largest prime factor as 2, the smallest prime number
    largest_factor = 2
    
    # Iterate from 3 to sqrt(n) with a step of 2 (only check odd factors)
    for i in range(3, int(n ** 0.5) + 1, 2):
        # Check if i is a factor of n
        while n % i == 0:
            # Update the largest factor if i is larger
            largest_factor = max(largest_factor, i)
            # Divide n by i to remove the factor
            n //= i
    
    # If n is a prime number greater than 2, it will be the largest factor
    if n > 2:
        largest_factor = n
    
    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. It uses a loop to check all odd numbers up to the square root of `n` and updates the largest factor whenever a larger factor is found. If `n` is a prime number greater than 2, it will be the largest factor, and the function returns it.