### Prime Number Checker
#### is_prime Function

```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:  # 1 and numbers less than 1 are not prime
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # all other even numbers are not prime
        return False
    # Check odd factors up to the square root of n
    for i in range(3, int(n ** 0.5) + 1, 2):
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

This script defines a function `is_prime(n)` that checks if a given integer `n` is prime. The function uses a simple trial division method, checking odd factors up to the square root of `n` to determine primality. It handles edge cases for `n = 1`, `n = 2`, and even numbers greater than `2`. The test cases provided in the docstring are then executed to verify the function's correctness.