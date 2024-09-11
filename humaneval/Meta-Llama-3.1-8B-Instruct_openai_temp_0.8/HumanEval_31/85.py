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
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check up to the square root of n
        if n % i == 0:  # If n is divisible by any number between 2 and its square root, it's not prime
            return False
    return True

# Test cases
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441)) # True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This script defines a function `is_prime(n)` that checks if a number `n` is prime. It first checks if `n` is less than or equal to 1, in which case it returns `False`. Then it checks divisibility from 2 to the square root of `n`, and if `n` is divisible by any of these numbers, it returns `False`. If `n` passes this check, it returns `True`. Finally, it tests this function with the given examples.