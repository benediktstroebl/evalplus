### Prime Number Checker
```python
def is_prime(n):
    """
    Return True if a given number is prime, and False otherwise.

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
    if n <= 1:  # 1 and numbers less than 1 are not prime
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # all other even numbers are not prime
        return False
    max_divisor = int(n**0.5) + 1  # only need to check up to the square root of n
    for d in range(3, max_divisor, 2):  # check odd numbers only
        if n % d == 0:
            return False
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
This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It returns `True` if `n` is prime and `False` otherwise. The function uses a simple algorithm to check for primality, which is efficient for large numbers. The script also includes test cases to demonstrate the function's behavior.