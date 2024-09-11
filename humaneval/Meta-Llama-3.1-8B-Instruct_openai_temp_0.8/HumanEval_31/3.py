Here's a Python script that defines the `is_prime` function according to the provided specifications:
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
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test the function
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```
This script defines the `is_prime` function and includes docstrings to document its behavior. It also includes example use cases and tests the function with the provided inputs.