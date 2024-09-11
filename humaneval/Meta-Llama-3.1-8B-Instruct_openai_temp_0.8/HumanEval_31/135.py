```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    
    A prime number is a positive integer that is divisible only by itself and 1.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if n is prime, False otherwise.
    
    Examples:
        >>> is_prime(6)
        False
        >>> is_prime(101)
        True
        >>> is_prime(11)
        True
        >>> is_prime(13441)
        True
        >>> is_prime(61)
        True
        >>> is_prime(4)
        False
        >>> is_prime(1)
        False
    """
    # Handle edge cases where n is less than 2
    if n < 2:
        return False
    
    # Check divisibility from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    # If no divisors are found, n is prime
    return True

# Test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime. It then tests this function with the provided test cases. The function uses a simple and efficient algorithm to check for primality: it checks divisibility from 2 to the square root of `n`, and returns False as soon as a divisor is found. If no divisors are found, it returns True.