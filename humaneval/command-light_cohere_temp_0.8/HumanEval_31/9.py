```python
def is_prime(n):
    """Check whether a given number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test code
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This code defines the function `is_prime(n)` that checks whether a given number is prime or not. It iterates through the specific case for an input of 6, which returns `False` since 6 is not a prime number. The function then iterates from 2 to the square root of the input number (up to the `int(n ** 0.5)` inclusive) and checks for divisibility. If the input number is divisible by any of the tested numbers, it returns `False`, indicating that the number is not prime. If no divisors are found, it returns `True`, indicating that the number is prime. The function also handles the edge case for input numbers less than or equal to 1 and passes all the tests.