```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
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
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(6))     # False
print(is_prime(101))   # True
print(is_prime(11))    # True
print(is_prime(13441)) # True
print(is_prime(61))    # True
print(is_prime(4))     # False
print(is_prime(1))     # False
```

This script uses a simple trial division method to check if a number is prime. It returns False for numbers less than 2 (since they are not prime), and for any number that has a divisor other than 1 and itself. Otherwise, it returns True, indicating that the number is prime. The script also includes the original test cases to ensure the function works correctly.