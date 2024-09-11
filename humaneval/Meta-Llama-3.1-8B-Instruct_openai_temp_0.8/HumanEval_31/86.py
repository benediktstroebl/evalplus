```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):
        # Check if the number has any divisors other than 1 and itself
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

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It returns `True` if the number is prime and `False` otherwise. The function uses a simple trial division method to check for primality, which is sufficient for small to medium-sized numbers. For larger numbers, a more efficient algorithm such as the Miller-Rabin primality test may be necessary. The test cases at the end of the script demonstrate the function's behavior with various inputs.