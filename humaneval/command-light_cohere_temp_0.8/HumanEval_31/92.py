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

This function, `is_prime`, takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. The function uses a simple algorithm to determine whether `n` is a prime number or not. It first checks for divisibility by 2 and 3, then uses a simple loop to check for divisibility by numbers within the square root of `n`.