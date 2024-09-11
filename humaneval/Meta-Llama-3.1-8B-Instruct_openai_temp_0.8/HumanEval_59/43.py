```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    
    Assume n > 1 and is not a prime.
    
    Parameters:
    n (int): A composite number greater than 1.
    
    Returns:
    int: The largest prime factor of n.
    
    Examples:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    
    def is_prime(num: int) -> bool:
        """
        Check if a number is prime.
        
        Parameters:
        num (int): The number to check.
        
        Returns:
        bool: True if num is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(n, 1, -1):
        # Check if i is a factor of n and prime
        if n % i == 0 and is_prime(i):
            return i

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. The function uses a helper function `is_prime` to check if a number is prime. It then iterates over the factors of `n` in descending order and returns the first prime factor it encounters.