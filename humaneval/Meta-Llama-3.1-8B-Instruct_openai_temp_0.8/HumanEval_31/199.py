### Prime Number Checker
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
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):
        # Check for divisors up to the square root of n
        if n % i == 0:
            # If n is divisible by i, it's not prime
            return False
    # If no divisors are found, n is prime
    return True

# Test cases
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441)) # True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```
This script defines a function `is_prime(n)` that checks whether a given number `n` is prime. It returns `True` if `n` is prime and `False` otherwise. The function uses a simple trial division method, which is sufficient for small to medium-sized numbers. For larger numbers, more efficient algorithms like the Miller-Rabin primality test may be needed.