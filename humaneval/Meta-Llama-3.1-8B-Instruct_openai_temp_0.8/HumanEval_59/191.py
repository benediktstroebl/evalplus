```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
        n: A composite integer greater than 1.
    
    Returns:
        The largest prime factor of n.
    
    Example:
        >>> largest_prime_factor(13195)
        29
        >>> largest_prime_factor(2048)
        2
    """
    # Start from the largest possible factor
    for i in range(n - 1, 1, -1):
        # Check if i is a factor of n
        while n % i == 0:
            # Check if i is a prime number
            if is_prime(i):
                # If it's prime, return it as the largest prime factor
                return i
            # If it's not prime, divide n by i to continue checking other factors
            n = n // i

def is_prime(num: int):
    """
    Check if a number is prime.
    
    Args:
        num: The number to check.
    
    Returns:
        True if num is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))  # Output: 2
```

This script uses a helper function `is_prime` to check if a number is prime. The `largest_prime_factor` function then iterates from the largest possible factor (n-1) down to 2, checking if each factor is prime. If it finds a prime factor, it returns it as the largest prime factor.