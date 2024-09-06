```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test function
def test_is_prime():
    print(is_prime(6))      # Output: False
    print(is_prime(101))  # Output: True
    print(is_prime(11))     # Output: True
    print(is_prime(13441))  # Output: True
    print(is_prime(61))     # Output: True
    print(is_prime(4))      # Output: False
    print(is_prime(1))      # Output: False
    print(is_prime(13))     # Output: False
    print(is_prime(7))     # Output: False
```

This Python code defines a function named `is_prime` that checks whether a given number is a prime. The function returns `True` if the number is prime and `False` otherwise. It uses several conditional checks and trial divisions to determine primality. 

The `test_is_prime` function serves as a test driver for the `is_prime` function. It prints the results of the function for various input values, which can be useful for testing and validating the correctness of the function.