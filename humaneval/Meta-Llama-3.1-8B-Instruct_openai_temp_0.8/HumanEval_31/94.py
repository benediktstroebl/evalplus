### Prime Number Checker
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    # Handle edge cases
    if n <= 1:
        return False

    # Check divisibility up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    # If no divisors are found, n is prime
    return True

# Test cases
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441))# True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```
This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It handles edge cases where `n` is less than or equal to 1, and then checks divisibility up to the square root of `n` using a loop. If no divisors are found, the function returns `True`, indicating that `n` is prime. The test cases at the end demonstrate the function's behavior for various inputs.