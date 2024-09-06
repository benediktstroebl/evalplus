Here is a Python script with a self-contained function that checks if a number is prime, and passes the corresponding tests:
```python
def is_prime(n):
    """Check if a given number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

The function `is_prime` accepts an integer `n` and then uses a loop to verify if `n` is divisible by any positive integer less than its square root and 1. The function returns `True` if `n` is a prime number and `False` otherwise.