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

# Unit tests
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This Python code defines a function named `is_prime(n)` that checks whether a given number `n` is a prime number or not. It uses a fact-based methods to perform this check: if `n` is less than or equal to 1, it's not prime; if `n` is of the form 2 or 3, it's a prime; otherwise, it checks the number's primality by iterating up to the square root of the number while taking modulo every possible divisor starting from 5.