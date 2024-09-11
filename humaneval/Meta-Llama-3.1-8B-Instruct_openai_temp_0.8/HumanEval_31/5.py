### Prime Number Checker
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

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
    elif n <= 3:
        # 2 and 3 are prime
        return True
    elif n % 2 == 0 or n % 3 == 0:
        # Numbers divisible by 2 or 3 are not prime
        return False
    i = 5
    while i * i <= n:
        # Check if n is divisible by any odd number up to its square root
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test the function
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```
This script defines a function `is_prime(n)` that checks whether a given number `n` is prime. The function uses a simple and efficient algorithm to determine primality. It first checks for special cases (numbers less than or equal to 1, numbers less than or equal to 3), then checks for divisibility by 2 and 3. Finally, it checks for divisibility by any odd number up to the square root of `n`. If `n` is not divisible by any of these numbers, it is prime.