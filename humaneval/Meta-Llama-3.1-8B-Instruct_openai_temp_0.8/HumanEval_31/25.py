```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

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
    # Corner cases: numbers less than 2 are not prime
    if n < 2:
        return False

    # Check if n is divisible by any number up to its square root
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If n is not divisible by any number up to its square root, it's prime
    return True

# Test the function
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441)) # True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This script defines a function `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is prime and `False` otherwise. The function first checks for corner cases where `n` is less than 2, and then checks if `n` is divisible by any number up to its square root. If `n` is not divisible by any number up to its square root, it's prime. The function is then tested with the provided examples.