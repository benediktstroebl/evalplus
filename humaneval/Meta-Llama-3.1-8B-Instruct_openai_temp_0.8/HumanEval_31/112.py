### Prime Number Checker
#### Problem Description
This script checks if a given number is prime or not.

#### Code
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check.

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
    if n <= 1:  # 1 and numbers less than 1 are not prime
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # All other even numbers are not prime
        return False
    # Check odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
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

#### Explanation
The `is_prime` function checks if a given number `n` is prime by following these steps:

1. Numbers less than or equal to 1 are not prime.
2. 2 is the only even prime number, so it's returned as `True` directly.
3. All other even numbers are not prime, so they're returned as `False` directly.
4. For odd numbers, we check odd factors up to the square root of `n`. If any factor is found, the number is not prime, so we return `False`.
5. If no factors are found, the number is prime, so we return `True`.