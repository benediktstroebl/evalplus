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
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):
        # Check if n has any divisors other than 1 and itself
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

This script defines a function `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is prime, and `False` otherwise. The function works by checking if `n` has any divisors other than 1 and itself. If `n` is less than or equal to 1, it is not prime, so the function immediately returns `False`. Otherwise, the function checks if `n` has any divisors between 2 and the square root of `n`. If any divisors are found, the function returns `False`. If no divisors are found, the function returns `True`, indicating that `n` is prime. The test cases at the end of the script demonstrate the function's behavior for various input values.