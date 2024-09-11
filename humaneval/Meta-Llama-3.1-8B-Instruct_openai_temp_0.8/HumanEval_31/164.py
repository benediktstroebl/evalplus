```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:  # 1 and numbers less than 1 are not prime
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # All other even numbers are not prime
        return False
    # Check odd factors up to the square root of n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
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

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime. It uses a simple trial division method, which checks for divisibility by odd numbers up to the square root of `n`. The function then returns `True` if `n` is prime and `False` otherwise. The test cases are included at the end to verify the function's correctness.