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
    # Handle edge cases
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check for odd factors
    max_factor = int(n ** 0.5) + 1
    for i in range(3, max_factor, 2):
        if n % i == 0:
            return False

    return True

# Test the function
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441)) # True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime. It handles the edge cases where `n` is less than or equal to 1, and where `n` is 2 or an even number. For odd numbers, it checks for factors up to the square root of `n`. If no factors are found, the function returns `True`, indicating that `n` is prime. The function is then tested with the provided examples.