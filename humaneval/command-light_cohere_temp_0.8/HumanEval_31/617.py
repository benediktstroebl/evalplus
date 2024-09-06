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

# Test case 1
print(is_prime(6))  # Output: False

# Test case 2
print(is_prime(101))  # Output: True

# Test case 3
print(is_prime(11))  # Output: True

# Test case 4
print(is_prime(13441))  # Output: True

# Test case 5
print(is_prime(61))  # Output: True

# Test case 6
print(is_prime(4))  # Output: False

# Test case 7
print(is_prime(1))  # Output: False
```

This Python code defines a function named `is_prime` that checks whether a given number is prime or not. It uses a basic prime number criteria and performs tests on various numbers to pass the corresponding tests and return the appropriate results.