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

# Test case 1: Is 6 a prime?
print(is_prime(6))  # Output: True

# Test case 2: Is 101 a prime?
print(is_prime(101))  # Output: True

# Test case 3: Is 441 a prime?
print(is_prime(13441))  # Output: True

# Test case 4: Is 61 a prime?
print(is_prime(61))  # Output: True

# Test case 5: Is 4 a prime?
print(is_prime(4))  # Output: False

# Test case 6: Is 1 a prime?
print(is_prime(1))  # Output: False
```