**Prime Number Checker**
=======================

A Python function to check if a given number is prime.

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.

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
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

# Test cases
print(is_prime(6))       # False
print(is_prime(101))     # True
print(is_prime(11))      # True
print(is_prime(13441))   # True
print(is_prime(61))      # True
print(is_prime(4))       # False
print(is_prime(1))       # False
```

This script defines a function `is_prime(n)` that checks if a given number `n` is prime. It returns `True` if the number is prime, and `False` otherwise. The function uses a simple trial division method to check for primality, which is sufficient for small to medium-sized integers.