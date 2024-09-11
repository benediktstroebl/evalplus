```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

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
    # Edge cases: numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check if the number is divisible by any number up to its square root
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    # If the number is not divisible by any number up to its square root, it's prime
    return True

# Example usage:
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It first checks for edge cases where `n` is less than 2, in which case it returns `False`. Then it iterates over numbers from 2 to the square root of `n` and checks if `n` is divisible by any of them. If it finds a divisor, it returns `False`. Otherwise, it returns `True`, indicating that `n` is prime. The script includes example usage to demonstrate the function's behavior.