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

This code defines a function `is_prime` that checks whether a given number is prime or not. It uses a first-degree primality tests (smaller than 2 and 3) and then employs a loop with the sqrt of the number to check for divisibility up to the square root. The function returns `True` if the number is prime and `False` otherwise.