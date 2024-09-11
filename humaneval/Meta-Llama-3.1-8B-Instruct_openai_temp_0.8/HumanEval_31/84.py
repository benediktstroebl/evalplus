### Prime Number Checker
#### Python Script

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # Edge case: numbers less than or equal to 1 are not prime
        return False
    elif n <= 3:  # Edge case: numbers less than or equal to 3 are prime
        return True
    elif n % 2 == 0 or n % 3 == 0:  # Edge cases: even numbers and multiples of 3 are not prime
        return False
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

This script defines a function `is_prime(n)` that checks whether a given integer `n` is prime. It uses a simple and efficient algorithm that first checks for edge cases (numbers less than or equal to 1, numbers less than or equal to 3, even numbers, and multiples of 3), and then uses a loop to check for divisibility by numbers up to the square root of `n`. The function returns `True` if `n` is prime and `False` otherwise. The script includes test cases to demonstrate the function's correctness.