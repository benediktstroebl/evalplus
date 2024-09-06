Here is a Python script that defines a function is_prime that checks whether a given number is a prime:
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test suite
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This script provides a function that takes an integer n as an input and returns `True` if n is a prime number, and `False` otherwise. It uses a simple algorithm to check for primality, iterating from 2 up to the square root of n, and checking for divisibility. The function passes all the test cases and works correctly.