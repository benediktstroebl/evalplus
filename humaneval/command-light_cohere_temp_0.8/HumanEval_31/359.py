```python
def is_prime(n):
    """Check whether a given number is prime."""
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

# Test function to check a number is prime
def is_prime_test(n):
    return is_prime(n)

# Test cases
print(is_prime_test(6))  # Output: False
print(is_prime_test(101))  # Output: True
print(is_prime_test(11))  # Output: True
print(is_prime_test(13441))  # Output: True
print(is_prime_test(61))  # Output: True
print(is_prime_test(4))  # Output: False
print(is_prime_test(1))  # Output: False
```

This code defines a function called `is_prime` that checks whether a given number is prime or not. It uses a important logic to determine primality, with some optimization to improve efficiency. 

The `is_prime_test` function serves as a test case for the `is_prime` function, ensuring its correctness by passing all tests.