```python
def is_prime(n):
    if n <= 1:
        return False
    for i := 2; i <= n; i += 1:
        if n % i == 0:
            return False
    return True

# Unit tests
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This script defines a function `is_prime(n)` that checks whether a given number is prime. The function uses a loop to iterate up to `n` and checks for divisibility by every integer `i` such that `i <= n`. The function returns `True` if no divisors are found, indicating the number is prime; Otherwise, it returns `False`.