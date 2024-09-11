```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
        n (int): A composite number greater than 1.
    
    Returns:
        int: The largest prime factor of n.
    
    Example:
        >>> largest_prime_factor(13195)
        29
        >>> largest_prime_factor(2048)
        2
    """
    def is_prime(num: int) -> bool:
        """
        Check if a number is prime.
        
        Args:
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

    largest_factor = 1
    for i in range(2, n + 1):
        # Check if i is a factor of n and a prime number
        if n % i == 0 and is_prime(i):
            largest_factor = max(largest_factor, i)
    
    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. The function uses a helper function `is_prime` to check if a number is prime. It iterates over the numbers from 2 to `n` (inclusive), checks if each number is a factor of `n` and a prime number, and keeps track of the largest such prime factor.