```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.

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

# Test cases
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441))# True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This code defines a function `is_prime(n)` that checks whether a number `n` is prime. It first checks if `n` is less than or equal to 1, in which case it's not prime. Then, it checks divisibility of `n` by all numbers from 2 to the square root of `n`. If it finds a divisor, it returns `False`, indicating that `n` is not prime. If no divisors are found, it returns `True`, indicating that `n` is prime. The test cases at the end of the script demonstrate its usage.