### Prime Number Checker
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself.

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
    if n == 2:
        # 2 is the only even prime number
        return True
    if n % 2 == 0:
        # If the number is even, it's not prime
        return False
    # Check odd factors up to the square root of n
    max_factor = int(n**0.5) + 1
    for i in range(3, max_factor, 2):
        if n % i == 0:
            # If n has an odd factor, it's not prime
            return False
    # If no factors are found, the number is prime
    return True

# Test cases
print(is_prime(6))    # False
print(is_prime(101))  # True
print(is_prime(11))   # True
print(is_prime(13441))# True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```
This script defines a function `is_prime(n)` that checks whether a given integer `n` is prime or not. It returns `True` if `n` is prime and `False` otherwise. The function uses a simple trial division method to check for factors. It first handles the edge cases of numbers less than or equal to 1, and then checks for factors up to the square root of `n`. If no factors are found, the number is prime. The script also includes test cases to demonstrate the function's behavior.