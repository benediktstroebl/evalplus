### Prime Number Checker
#### Python Script

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Handle edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check for factors up to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

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

This script defines the `is_prime` function that checks whether a given number `n` is prime or not. It handles edge cases where `n` is less than or equal to 1, and where `n` is 2 or 3 (which are prime). Then it checks for factors up to the square root of `n`, starting from 5 and increasing by 6 each time. This is because all primes are of the form `6k ± 1` with the exception of 2 and 3. If no factors are found, the function returns `True`, indicating that `n` is prime.