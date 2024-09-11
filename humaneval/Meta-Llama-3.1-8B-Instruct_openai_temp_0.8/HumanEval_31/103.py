```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
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
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
print(is_prime(6))
print(is_prime(101))
print(is_prime(11))
print(is_prime(13441))
print(is_prime(61))
print(is_prime(4))
print(is_prime(1))
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime. The function works by checking divisibility of `n` from 2 to the square root of `n`. If `n` is divisible by any number within this range, it is not prime and the function returns `False`. If `n` is not divisible by any number within this range, it is prime and the function returns `True`. The script also includes test cases to demonstrate the function's behavior.