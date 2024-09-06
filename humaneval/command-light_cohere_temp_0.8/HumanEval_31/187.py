```python
def is_prime(n):
    """Returns True if the number is prime, else False."""
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

This Python function, `is_prime`, returns `True` if the given number is prime and `False` otherwise. The function employs a fundamental primality testing strategies, such as checking divisibility by 2 and 3, and then utilizing the `sqrt` rule to determine if the number is prime. The function is self-contained, and it passes all the test cases provided.