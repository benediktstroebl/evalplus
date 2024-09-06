Here is a self-contained Python script that solves the problem of checking whether a given number is a prime number, and passes the tests you have provided:
```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
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

# Test cases
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This Python code defines a function named `is_prime` that checks whether a given number `n` is a prime number. It utilizes an set of rules and iterations to determine primality. The function returns `True` if the number is prime and `False` otherwise. The test cases at the specific numbers and the function is used to verify its correctness.