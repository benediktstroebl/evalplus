```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.

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
    # Handle edge cases
    if n <= 1:
        return False
    
    # Check if n is divisible by any number up to its square root
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    # If no divisors are found, the number is prime
    return True

# Test the function
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This Python function, `is_prime(n)`, checks whether a given number `n` is prime. It first handles edge cases by returning `False` for numbers less than or equal to 1. Then, it checks for divisibility by any number up to the square root of `n`, as any factor larger than the square root would have a corresponding factor smaller than the square root. If no divisors are found, the function returns `True`, indicating that the number is prime. Otherwise, it returns `False`.