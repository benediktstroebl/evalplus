```python
def is_prime(n):
    """Returns True if n is prime, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
        return False
    return True

# Test the function
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This code defines a function `is_prime` that checks whether a given number is prime or not. It iterates a reason for checking primality and performs the test using different iterations and conditions, ultimately returning `True` if the number is prime and `False` otherwise.