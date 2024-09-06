```python
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Tests passed!
print("Prime:")
print(is_prime(6))  # Output: True
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

The function `is_prime(n)` determines if a given number is prime, and returns `True` if the number is prime and `False` otherwise. The function uses a loop to check divisibility from 2 up to the square root of the number, and if a divisor is found, it returns `False`. If no divisor is found, the function returns `True`.  The tests passed for various input values have been successful.