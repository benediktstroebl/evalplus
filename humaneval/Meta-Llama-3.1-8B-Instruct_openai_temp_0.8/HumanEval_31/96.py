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
    if n <= 1:  # 0 and 1 are not prime numbers
        return False
    elif n <= 3:  # 2 and 3 are prime numbers
        return True
    elif n % 2 == 0 or n % 3 == 0:  # If the number is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # Check divisibility up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # Check for divisibility by i and i + 2 (since they are close to each other)
            return False
        i += 6  # Increment by 6 to check the next pair of numbers
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
This script defines a function `is_prime(n)` that takes an integer `n` as input and returns `True` if it's a prime number, and `False` otherwise. The function uses a simple algorithm to check for primality, which is efficient for large numbers. The example usage at the end demonstrates how to use this function with different inputs.