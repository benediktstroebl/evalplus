### Prime Number Checker
#### A Python Function to Check if a Number is Prime

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Handle edge cases
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check for divisibility up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    # If no divisors are found, the number is prime
    return True

# Example use cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script defines a function `is_prime(n)` that takes an integer `n` as input and returns `True` if it's a prime number, and `False` otherwise. The function uses a simple trial division approach to check for divisibility up to the square root of `n`, which is an optimization to reduce the number of iterations. The example use cases demonstrate the function's behavior with various inputs.