### Prime Number Checker
#### A Python Function to Determine if a Number is Prime

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

    # Prime numbers must be greater than 1
    if n <= 1:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # All other even numbers are not prime
    if n % 2 == 0:
        return False

    # Check odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    # If no factors are found, the number is prime
    return True

# Example usage:
print(is_prime(6))    # False
print(is_prime(101))  # True
print(is_prime(11))   # True
print(is_prime(13441))# True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. The function uses a simple trial division method to check for factors up to the square root of `n`. If any factors are found, the function returns `False`; otherwise, it returns `True`, indicating that the number is prime. The function also includes some basic optimizations, such as checking for even numbers and returning immediately if `n` is less than or equal to 1.