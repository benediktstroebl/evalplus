### Prime Number Checker
#### Python Script

Below is a Python script that checks whether a given number is prime or not.

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # 1 and numbers less than 2 are not prime
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # all other even numbers are not prime
        return False
    # Check odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(6))     # False
print(is_prime(101))   # True
print(is_prime(11))    # True
print(is_prime(13441)) # True
print(is_prime(61))    # True
print(is_prime(4))     # False
print(is_prime(1))     # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It returns `True` if the number is prime and `False` otherwise. The function uses a simple trial division method to check for primality. It first checks if the number is less than or equal to 1 (in which case it's not prime), then checks if it's 2 (the only even prime number). If the number is even but not 2, it's not prime. Otherwise, it checks odd factors up to the square root of the number. If any of these checks fail, the function returns `False`, indicating that the number is not prime. If all checks pass, the function returns `True`, indicating that the number is prime.